from sqlalchemy import (Column, Integer, String, Float, Sequence,
                         Identity, ForeignKey, delete, create_engine)

from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.dialects.postgresql import insert

from flask import Flask, jsonify


app = Flask(__name__)
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, Sequence('product_id_seq'), primary_key=True)
    title = Column(String(100), default=False)
    count = Column(Integer, default=0)
    price = Column(Float, default=0.0)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref="products")

    def __repr__(self):
        return '<Product %r>' % self.title

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    num = Column(Integer, Identity(minvalue=100, maxvalue=150, cycle=True))


    def __repr__(self):
        return '<User %r>' % self.name

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# @app.before_request
# def before_request():
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)
#
#     objects = [
#         User(name='Richard', surname='Gir'),
#         User(name='Adam', surname='Won'),
#         User(name='Ben', surname='Stiller'),
#         Product(title='Car', user_id=2),
#         Product(title='House', user_id=3),
#         Product(title='Helicopter', user_id=1),
#     ]
#
#     session.bulk_save_objects(objects)
#     session.commit()


@app.route('/products', methods=['DELETE'])
def delete_product(id: int):
    result = delete(Product).returning(Product.id, Product.title).where(Product.id == id)
    delete_row = session.execute(result).fetchone()
    if delete_row:
        delete_row_json = dict(id=delete_row.id, title=delete_row.title)
        return jsonify(delete_row_attrs=delete_row_json)

@app.route('/products', methods=['POST'])
def insert_product():
    insert_row = insert(Product).values(id=2, title="New product")
    # do_nothing = insert_row.on_conflict_do_nothing()
    do_update = insert_row.on_conflict_do_update(
        constraint='products_pkey',
        set_=dict(title="Google")
    )
    # session.execute(do_nothing)
    session.execute(do_update)
    session.commit()
    return "", 200

@app.route('/products', methods=['GET'])
def get_products():
    query = session.query(Product).all()
    products_list = []
    for p in query:
        product_obj = p.to_json()
        product_obj['user'] = p.user.to_json()
        products_list.append(product_obj)
    return jsonify(products=products_list)




if __name__ == '__main__':
    app.run(debug=True)
