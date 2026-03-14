from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import loguru

logger = loguru.logger
db = SQLAlchemy()



def create_app():
    _app = Flask(__name__)
    _app.config["TESTING"] = True
    _app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hw_test.db"
    db.init_app(_app)

    from .models import Client #, Parking, ClientParking

    @_app.before_request
    def before_request():
        db.create_all()

    @_app.teardown_appcontext
    def teardown(exception=None):
        db.session.remove()

    @_app.route('/clients', methods=['GET', 'POST'])
    def route_clients():
        if request.method == 'GET':
            response = db.session.query(Client).all()
            clients_list = [cli.to_json() for cli in response]
            return jsonify(clients_list), 200
        elif request.method == 'POST':
            try:
                # data = request.get_json()
                # if not data:
                id = request.form.get('id')
                name = request.form.get('name')
                surname = request.form.get('surname')
                credit_card = request.form.get('credit_card')
                car_number = request.form.get('car_number')
                # else:
                #     id = data['id']
                #     name = data['name']
                #     surname = data['surname']
                #     credit_card = data['credit_card']
                #     car_number = data['car_number']

                new_client = Client(
                    id=int(id),
                    name=name,
                    surname=surname,
                    credit_card=credit_card,
                    car_number=car_number
                )
                logger.info(f'New client created: {new_client}')
                db.session.add(new_client)
                db.session.commit()
                return jsonify(status="OK"), 201
            except Exception as e:
                return jsonify(status=f"ERROR {e}"), 400

    @_app.route('/clients/<int:client_id>')
    def get_client_by_id(client_id:int=None):
        pass



    return _app
