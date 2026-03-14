import pytest
import sys, pprint
from flask import template_rendered

pprint.pprint(sys.path)
from ..src.app import create_app, db as _db
from ..src.models import User, Product


@pytest.fixture
def app():
    __app = create_app()
    __app.config['DEBUG'] = False
    __app.config['TESTING'] = True
    __app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

    with __app.app_context():
        _db.create_all()
        user = User(
            name="TestBob",
            email='testing@gmail.com'
        )
        product = Product(
            name="TestProduct",
            price=100.0,
            user_id=1
        )
        _db.session.add(user)
        _db.session.add(product)
        _db.session.commit()

        yield __app
        _db.session.close()
        _db.drop_all()


@pytest.fixture
def client(app):
    client = app.test_client()
    yield client


@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield record
    finally:
        template_rendered.disconnect(record, app)

@pytest.fixture
def db(app):
    with app.app_context():
        yield _db





