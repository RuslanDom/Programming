from sqlalchemy import create_engine, Column, Integer, String, delete, update
from flask import Flask, jsonify, abort, request
from sqlalchemy.orm import declarative_base, sessionmaker


# config
app = Flask(__name__)
engine = create_engine('sqlite:///pythonsql.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    price = Column(Integer, default=0)
    count = Column(Integer, default=0)

    def __repr__(self):
        return f"<Product(title={self.title}, price={self.price}, count={self.count})>"

    def to_json(self):
        """Метод для удобной отдачи данных в виде словаря"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# При первом запросе будет создана БД
@app.before_request
def before_request():
    Base.metadata.create_all(engine)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/products", methods=["GET"])
def get_all_products():
    """Получение списка товаров на складе"""
    prods = session.query(Product).all()
    prods_list = []
    for prod in prods:
        prods_list.append(prod.to_json())
    return jsonify(prods_list=prods_list), 200


@app.route("/product/<int:id>", methods=["GET"])
def get_product(id: int):
    """Получение товара по ID"""
    prod = session.query(Product).filter_by(id=id).one_or_none()
    if prod is None:
        abort(404)
    return jsonify(prod.to_json()), 200


@app.route("/products", methods=["POST"])
def add_product():
    """Добавление нового продукта"""
    title = request.form.get('title', type=str)
    price = request.form.get('price', type=int)
    count = request.form.get('count', type=int)
    new_product = Product(title=title, price=price, count=count)
    session.add(new_product)
    session.commit()
    return jsonify(new_product.to_json()), 201


@app.route("/product/<int:id>", methods=["DELETE"])
def delete_product(id: int):
    """Удаление продукта по ID"""
    session.query(Product).filter_by(id=id).delete()
    session.commit()
    return jsonify({"message": "Product deleted"}), 204
    # Другой способ удаления с помощью конструкции delete из sqlalchemy
    # from sqlalchemy import delete
    # query = delete(Product).where(Product.id == id)
    # Можно сделать print(query)
    # session.execute(query)
    # session.close()


@app.route("/product/<int:id>", methods=["PATCH"])
def update_product(id: int):
    """Обновить продукт"""
    title = request.form.get('title', type=str)
    price = request.form.get('price', type=int)
    count = request.form.get('count', type=int)
    # 1 вариант
    prod = session.query(Product).filter_by(id=id).one_or_none()
    if title:
        prod.title = title
    if price:
        prod.price = price
    if count:
        prod.count = count
    session.commit()
    # 2 вариант
    # session.query(Product).filter_by(id=id).upload(
    #     {
    #         Product.title: title,
    #         Product.price: price,
    #         Product.count: count}
    # )
    # session.commit()
    # 3 вариант
    # from sqlalchemy import upload
    # query = upload(Product).where(Product.id == id).values(title=title, price=price, count=count)
    # Можно сделать print(query)
    # session.execute(query)
    # session.commit()
    return jsonify({"message": "Product upload"}), 200

if __name__ == "__main__":
    app.run(debug=True)





