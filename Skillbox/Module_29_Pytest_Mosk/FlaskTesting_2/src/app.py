from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from typing import List
import loguru

db = SQLAlchemy()
logger = loguru.logger

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prod.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .models import Product, User

    @app.before_request
    def before_request():
        # db.drop_all()
        logger.info(f'Create DB')
        db.create_all()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    @app.route('/test_route')
    def math_route():
        number = int(request.args.get('number', 0))
        result = number ** 2
        return jsonify({'result': result})

    @app.route('/users', methods=['POST'])
    def add_user():
        name = request.form.get('name', type=str)
        email = request.form.get('email', type=str)

        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'result': new_user.id}), 201


    @app.route('/users', methods=['GET'])
    def get_users():
        users = db.session.query(User).all()
        users_list = [u.to_json() for u in users]
        return jsonify(users_list), 200

    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_users_by_id(user_id: int):
        user = db.session.query(User).get(user_id)
        return jsonify(user.to_json()), 200


    @app.route('/products', methods=['POST'])
    def add_products():
        name = request.form.get('name', type=str)
        price = request.form.get('price', type=str)
        user_id = request.form.get('user_id', type=int)

        # user = db.session.query(User).where(User.id == user_id).first()
        new_product = Product(name=name, price=price, user_id=user_id)
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'result': new_product.id}), 201

    @app.route('/products', methods=['GET'])
    def get_products():
        logger.info("Start get products")
        products = db.session.query(Product).all()
        logger.info("Complete")
        products_list = []
        for product in products:
            user = db.session.query(User).where(User.id == product.user_id).first()
            product_obj = dict(**product.to_json(), user_id=user.to_json())
            logger.info(product_obj)
            products_list.append(product_obj)
        # return jsonify(products_list), 200
        return render_template("user_products.html", products=products_list), 200

    return app


