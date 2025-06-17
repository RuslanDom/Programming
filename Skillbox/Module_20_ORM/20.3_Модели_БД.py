from sqlalchemy import (Table, MetaData, create_engine, Column, Integer,
                        String, UniqueConstraint, Index)
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import sessionmaker, registry, declarative_base

# config
engine = create_engine("sqlite:///pythonsql.db")
Session = sessionmaker(bind=engine)
session = Session()

"""
КЛАССИЧЕСКИЙ СТИЛЬ
----------------------------------------------------------------------------
"""
# classic config
metadata = MetaData()
mapper_registry = registry()  # Для связывания объекта Table(сущность таблицы) и объекта User(отображения класса)


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(30), nullable=False),
    Column("email", String(50)),
    Column("login", String(30), nullable=False)
)

class User:
    def __init__(self, name, email, login):
        self.name = name
        self.email = email
        self.login = login

    def __repr__(self):
        return f"Name: {self.name} Email: {self.email} Login: {self.login}"


# Создание таблицы классическим способом

mapper_registry.map_imperatively(User, users)
metadata.create_all(bind=engine)

"""
ДЕКЛАРАТИВНЫЙ СТИЛЬ
-------------------------------------------------------------------------------------------
"""
# Декларативный подход создания таблиц в БД
Base = declarative_base()

class Animal(Base):
    __tablename__ = "animals"
    # Index - добавляет индекс, UniqueConstraint - проверяет на уникальность
    __table_args__ = (Index("name_index", "name"), UniqueConstraint("name"))
    __mapper_args__ = {"polymorphic_identity": "animal"}
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return f"Name: {self.name} Age: {self.age}"

    @classmethod
    def get_all_users(cls):
        return session.query(User).all()

    @classmethod
    def get_name_user(cls, name):
        try:
            name = session.query(User).filter_by(name=name).one()
            return name
        except NoResultFound:
            print("Животное не существует")
        except MultipleResultsFound:
            print("Животных с этим именем больше одного")

# Создание таблицы используя декларативный подход
Base.metadata.create_all(bind=engine)