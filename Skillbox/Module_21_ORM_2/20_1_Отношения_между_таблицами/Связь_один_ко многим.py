from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, registry

# config
engine = create_engine("sqlite:///db_folder/one_to_many.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Классический стиль
# mapper_registry = registry()

class Admin(Base):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True)
    name = Column(String, default="admin")
    password = Column(String, default="admin")

    # двунаправленная связь нужно определять в обоих классах
    # users = relationship("User", back_populates="admin")

    # альтернативный вариант двунаправленной связи
    # (в отличие от back_populates не нужно определять в обеих таблицах)
    users = relationship("User", backref="admin")

    def __repr__(self):
        return f"name: {self.name}, password: {self.password}"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    chief = Column(Integer, ForeignKey("admin.id"), default=1)

    # двунаправленная связь нужно определять в обоих классах
    # parents = relationship("Admin", back_populates="users")

    def __repr__(self):
        return f"name: {self.name}, password: {self.password}, chief: {self.chief}"

# Классический стиль связывания 2 таблиц
# mapper_registry.map_imperatively(Admin, properties={
#     "users": relationship(User)
#         }
#     )


"""
----------------------- Основная часть ------------------------
"""
class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    children = relationship("Child", back_populates="parents")

    def __repr__(self):
        return f"name: {self.name}"


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("parent.id"))
    parents = relationship("Parent", back_populates="children")

    def __repr__(self):
        return f"name: {self.name}"

def admin_users():
    try:
        # start
        Base.metadata.create_all(bind=engine)
        query = Admin(name="Ruslan", password="qwerty")
        session.add(query)
        session.commit()

        query = Admin(name="Kristina", password="fff")
        session.add(query)
        session.commit()

        query = User(name="Bogdan", password="123", chief=1)
        session.add(query)
        session.commit()

        query = User(name="Zlata", password="321", chief=2)
        session.add(query)
        session.commit()

    finally:
        session.close()


def parent_children():
    try:
        Base.metadata.create_all(bind=engine)
        parent = Parent(name="Ruslan")
        session.add(parent)
        session.commit()
        child_one = Child(name="Bogdan", parent_id=1)
        child_two = Child(name="Zlata", parent_id=1)
        session.add(child_one)
        session.add(child_two)
        session.commit()

        my_children = session.query(Child).all()
        parents = session.query(Parent).first()

        print(my_children)
        print(parents)
    finally:
        session.close()


if __name__ == "__main__":
    # admin_users()
    parent_children()

