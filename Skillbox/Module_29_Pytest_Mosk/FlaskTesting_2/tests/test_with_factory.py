from .factories import UserFactory, ProductFactory
from ..src.models import User, Product

def test_create_user(app, db):
    user = UserFactory()
    db.session.commit()
    assert user.id is not None
    assert len(db.session.query(User).all()) > 1

def test_create_product(app, db):
    product = ProductFactory()
    db.session.commit()
    assert product.id is not None
    assert product.user_id is not None
    assert len(db.session.query(Product).all()) > 1