from ..src.app import create_app, db
from ..src.models import User, Product

import factory
import factory.fuzzy as fuzzy
import random


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    name = factory.Faker("first_name")
    email = factory.LazyAttribute(lambda o: '%s@gmail.com' % o.name)


class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Product
        sqlalchemy_session = db.session

    name = fuzzy.FuzzyText(prefix="Product ")
    price = factory.LazyAttribute(lambda o: '%.2f' % random.randint(1, 100))
    user_id = factory.LazyAttribute(lambda o: '%d' % random.randint(1, 10))
    # user = factory.SubFactory(UserFactory) - в поле таблицы можно создать рандомный объект и поместить в него

