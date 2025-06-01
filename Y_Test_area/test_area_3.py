from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from flask import Flask, request, abort, jsonify
from flasgger import Schema, fields, ValidationError, Swagger, APISpec
from marshmallow import validate, post_load
from flask_restx import Api, Resource
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

app = Flask(__name__)
engine = create_engine("sqlite:///sqlworker.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
api = Api(app)
spec = APISpec(
    title="Workers",
    version="1.0.0",
    openapi_version="2.0.0",
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin()
    ]

)


class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    age = Column(Integer, default=0)
    gender = Column(String(10), default='')

    def __repr__(self):
        return f"Name: {self.name} Age: {self.age} Gender: {self.gender}"

    def to_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class WorkerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    age = fields.Int(default=0)
    gender = fields.Str(default='')

    @post_load
    def get_worker(self, data: dict, **kwargs) -> Worker:
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
            definitions: Получить список работников
            schema:
              type: array
              items:
                $ref: '#/definitions/Worker'

        """
        schema = WorkerSchema()
        workers = session.query(Worker).all()
        worker_list = []
        for w in workers:
            worker_list.append(w.to_json())
        return schema.dump(worker_list, many=True), 200


    def post(self):
        """
        Add new worker
        ---
        tags:
          - workers
        parameters:
          - in: body
            name: new worker
        responses:
          201:
            definitions: Добавление нового работника
            schema:
              $ref: '#/definitions/Worker'

        """
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        new_worker = Worker(name=name, age=age, gender=gender)
        schema = WorkerSchema()
        session.add(new_worker)
        session.commit()
        return schema.dump(new_worker), 201

@api.route("/workers/<int:id>")
class WorkerId(Resource):
    def get(self, id: int):
        schema = WorkerSchema()
        worker = session.query(Worker).filter_by(id=id).one_or_none()
        if not worker:
            abort(404)
        return schema.dump(worker), 200


    def delete(self, id: int):
        w = session.query(Worker).filter_by(id=id).one_or_none()
        if not w:
            abort(404)
        session.query(Worker).filter_by(id=id).delete()
        session.commit()
        return "Success", 204


    def patch(self, id: int):
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        worker = session.query(Worker).filter_by(id=id).one_or_none()
        if not worker:
            abort(404)
        if name:
            worker.name = name
        if age:
            worker.age = age
        if gender:
            worker.gender = gender
        session.commit()
        return jsonify(worker.to_json()), 200


template = spec.to_flasgger(
    app=app,
    definitions=[WorkerSchema]
)
swagger = Swagger(app=app, template=template)


if __name__ == "__main__":
    app.run(debug=True)