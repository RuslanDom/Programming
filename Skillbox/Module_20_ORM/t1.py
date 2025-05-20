# import json
#
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import declarative_base, sessionmaker
# from flask import Flask, request, abort, jsonify
#
# # config
# app = Flask(__name__)
# engine = create_engine("sqlite:///pythonsql.db")
# Base = declarative_base()
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
# class Worker(Base):
#     __tablename__ = "workers"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(30), nullable=False)
#     age = Column(Integer, default=0)
#     status = Column(String(20), default="Free")
#
#     def __repr__(self):
#         return f"Name: {self.name}, Age: {self.age}, Status: {self.status}"
#
#     def json_to(self):
#         return {w.name: getattr(self, w.name) for w in self.__table__.columns}
#
#
# @app.before_request
# def start():
#     Base.metadata.create_all(engine)
#
# @app.route("/")
# def hello():
#     return "Hello workers"
#
# @app.route("/workers", methods=["GET"])
# def get_all_workers():
#     workers = session.query(Worker).all()
#     workers_list = []
#     for w in workers:
#         workers_list.append(w.json_to())
#     return jsonify(workers=workers_list), 200
#
# @app.route("/workers", methods=["POST"])
# def add_new_worker():
#     w_name = request.form.get("name", type=str)
#     w_age = request.form.get("age", type=int)
#     w_status = request.form.get("status", type=str)
#     new_worker = Worker(name=w_name, age=w_age, status=w_status)
#     session.add(new_worker)
#     session.commit()
#     return jsonify(new_worker.json_to()), 201
#
# @app.route("/workers/<int:id>", methods=["GET"])
# def get_worker_by_id(id: int):
#     worker = session.query(Worker).filter_by(id=id).one_or_none()
#     if worker is None:
#         abort(404)
#     return jsonify(worker.json_to()), 200
#
# @app.route("/workers/<int:id>", methods=["DELETE"])
# def delete_worker(id: int):
#     session.query(Worker).filter_by(id=id).delete()
#     session.commit()
#     return "Delete worker, successfully", 204
#
# @app.route("/workers/<int:id>", methods=["PATCH"])
# def update_worker(id: int):
#     worker = session.query(Worker).filter_by(id=id).one_or_none()
#     data: dict = request.get_json()
#     if data.setdefault("name"):
#         worker.name = data["name"]
#     if data.setdefault("age"):
#         worker.age = data["age"]
#     if data.setdefault("status"):
#         worker.status = data["status"]
#
#     # w_name = request.form.get("name")
#     # w_age = request.form.get("age")
#     # w_status = request.form.get("status")
#     # if w_name:
#     #     worker.name = w_name
#     # if w_age:
#     #     worker.age = w_age
#     # if w_status:
#     #     worker.status = w_status
#
#     session.commit()
#     return jsonify(worker.json_to()), 200
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
#




from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from flask import Flask, request, jsonify, abort


app = Flask(__name__)
engine = create_engine("sqlite:///pythonsql.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()



class Animal(Base):
    __tablename__ = "Animal"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    age = Column(Integer, default=0)
    view = Column(String(20), default=None)

    def __repr__(self):
        return f"Name: {self.name} Age: {self.age} View: {self.view}"

    def to_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

@app.before_request
def start():
    Base.metadata.create_all(engine)

@app.route("/")
def hello():
    return "Hello"


@app.route("/animals", methods=["GET"])
def get_all_animals():
    animals = session.query(Animal).all()
    animals_list = []
    for ani in animals:
        animals_list.append(ani.to_json())
    return jsonify(animals=animals_list), 200


@app.route("/animals", methods=["POST"])
def add_new_animal():
    name = request.form.get("name")
    age = request.form.get("age")
    view = request.form.get("view")
    new_animal = Animal(name=name, age=age, view=view)
    session.add(new_animal)
    session.commit()
    return jsonify(new_animal=new_animal.to_json()), 201


@app.route("/animals/<int:id>", methods=["DELETE"])
def delete_animal(id: int):
    session.query(Animal).filter_by(id=id).delete()
    session.commit()
    return {"message": "Success"}, 204


@app.route("/animals/<int:id>", methods=["PATCH"])
def update_animal(id: int):
    data: dict = request.get_json()
    animal = session.query(Animal).filter_by(id=id).one()
    if data.setdefault("name"):
        animal.name = data["name"]
    if data.setdefault("age"):
        animal.age = data["age"]
    if data.setdefault("view"):
        animal.view = data["view"]
    session.commit()
    return jsonify(animal=animal.to_json()), 200


@app.route("/animals/<int:id>", methods=["GET"])
def get_animal_by_id(id: int):
    animal = session.query(Animal).filter_by(id=id).one_or_none()
    if animal is None:
        abort(404)
    return jsonify(animal=animal.to_json()), 200

if __name__ == "__main__":
    app.run(debug=True)























































