from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from flask import Flask, request, abort, jsonify
from flask_restx import Resource, Api
from flasgger import APISpec, Schema, fields, Swagger
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import post_load

app = Flask(__name__)
api = Api(app)
spec = APISpec(
    title="Workers",
    version="1.0.0",
    openapi_version="2.0.0",
    plugins=[
        MarshmallowPlugin(),
        FlaskPlugin()
    ]
)
engine = create_engine("sqlite:///worker_data.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Worker(Base):
    __tablename__ = "workers_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    age = Column(Integer, default=0)
    gender = Column(String(10), default="unknown")

    def __repr__(self):
        return f"Name: {self.name} Age: {self.age} Gender: {self.gender}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__columns}

class WorkerSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    age = fields.Integer(default=0)
    gender = fields.String(default="unknown")

    @post_load
    def get_worker_obj(self, name, age, gender, **kwargs):
        return Worker(name=name, age=age, gender=gender)

    # Получить данные с json словаря
    # @post_load
    # def get_worker_obj(self, data: dict, **kwargs):
    #     return Worker(**data)


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
            definitions: Get all workers in database
            type:
              array
            items:
              $ref: '#/definitions/Worker'
        """
        schema = WorkerSchema()
        workers = session.query(Worker).all()
        worker_list = []
        for w in workers:
            worker_list.append(w)
        return schema.dump(worker_list, many=True), 200

    def post(self):
        """
        Add wen worker
        ---
        tags:
          - workers
        parameters:
          - in: body
            name:
              new_worker
            schema:
              $ref: '#/definitions/Worker'
            example:
              name: John
              age: 100
              gender: male
        responses:
          201:
            definitions: Add new worker in database
            schema:
              type: object
              $ref: '#/definitions/Worker'
        """
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        schema = WorkerSchema()
        worker: Worker = schema.get_worker_obj(name, age, gender)
        # Через json словарь
        # data = request.get_json()
        # worker: Worker = schema.get_worker_obj(data)
        session.add(worker)
        return schema.dump(worker), 201

template = spec.to_flasgger(
    app=app,
    definitions=[WorkerSchema]
)
swagger = Swagger(app=app, template=template)

if __name__ == "__main__":
    app.run(debug=True)




