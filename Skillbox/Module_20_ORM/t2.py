from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from flask import Flask, request, jsonify
from flask_restx import Resource, Api
from flasgger import Schema, APISpec, Swagger, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import post_load


app = Flask(__name__)
api = Api(app)
engine = create_engine("sqlite:///sqlpython.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
spec = APISpec(
    title='Workers',
    version="1.0.0",
    openapi_version="2.0.0",
    plugins=[
        MarshmallowPlugin(),
        FlaskPlugin()
    ]
)



class Worker(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, default=0)
    gender = Column(String, default="")

    def __repr__(self):
        return f"Name: {self.name} Age: {self.age} Gender: {self.gender}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}



class WorkerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    age = fields.Int(default=0)
    gender = fields.Str(default='')

    @post_load
    def get_obj(self, data, **kwargs):
        return Worker(**data)

@app.before_request
def start_app():
    Base.metadata.create_all(engine)


@api.route("/workers")
class Workers(Resource):
    def get(self):
        """
        Get all workers
        ---
        tags:
          - workers
        responses:
          200:
            definitions: Получить всех работников
            schema:
              type: array
              items:
                $ref: '#/definitions/Worker'
        """

        workers = session.query(Worker).all()
        schema = WorkerSchema()
        w_list = []
        for w in workers:
            w_list.append(w.to_json())
        return schema.dump(w_list, many=True), 200

    def post(self):
        """
        Add new worker
        ---
        tags:
          - workers
        parameters:
          - in: body
            name: Add new worker
            schema:
              $ref: '#/definitions/Worker'
        responses:
          201:
            definitions: Добавить нового работника
            schema:
              type: object
              $ref: '#/definitions/Worker'
        """
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        worker = Worker(name=name, age=age, gender=gender)
        schema = WorkerSchema()
        session.add(worker)
        session.commit()
        return schema.dump(worker), 201


template = spec.to_flasgger(app=app, definitions=[WorkerSchema])
swagger = Swagger(app=app, template=template)


if __name__ == "__main__":
    app.run(debug=True)


