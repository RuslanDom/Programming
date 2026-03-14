from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import declarative_base
from .app import db





class User(db.Model):
    __tablename__ = 'users'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    email: str = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f'<User(id={self.id}, name={self.name}, email={self.email})>'

    def to_json(self) -> dict:
        return {"id": self.id, "name": self.name, "email": self.email}


class Product(db.Model):
    __tablename__ = 'products'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    price: float = Column(Float, nullable=False, default=0.0)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __repr__(self) -> str:
        return f'<Product(id={self.id}, name={self.name}, price={self.price}, user_id={self.user_id})>'

    def to_json(self) -> dict:
        return {"id": self.id, "name": self.name, "price": self.price}