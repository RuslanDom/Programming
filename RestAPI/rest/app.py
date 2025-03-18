from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets_data.db'
db = SQLAlchemy(app)


class Pets(db.Model):
    id: db.Integer = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: db.String = db.Column(db.String(50), nullable=False)
    kind: db.String = db.Column(db.String(50), nullable=False)
    breed: db.String = db.Column(db.String(50), nullable=True, default="UNKNOWN")

    def __repr__(self):
        return f"This is {self.kind}, it`s name: {self.name}, breed: {self.breed}"


@app.route('/pets', methods=['GET'])
def get_pets():
    data = Pets.query.all()
    response = [{"Кличка": pet.name, "Вид животного": pet.kind, "Порода": pet.breed} for pet in data]
    return jsonify({"pets": response}), 200, {"Content-Type": "application/json"}

@app.route('/pets', methods=['POST'])
def add_pet():
    name = request.json['name']
    kind = request.json['kind']
    breed = request.json['breed']
    pet = Pets(name=name, kind=kind, breed=breed)
    db.session.add(pet)
    db.session.commit()
    return jsonify({"success": True}), 201, {"Content-Type": "application/json"}


@app.route('/pets/<string:name>')
def get_pet_name(name):
    try:
        pet = Pets.query.filter_by(name=name).first()
        return jsonify({"Name": pet.name, "Kind": pet.kind, "Breed": pet.breed}), 200, {"Content-Type": "application/json"}
    except Exception as e:
        return jsonify({"error": "This is pet not found"}), 404, {"Content-Type": "application/json"}


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)

