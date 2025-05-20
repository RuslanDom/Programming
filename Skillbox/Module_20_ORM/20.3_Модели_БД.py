from sqlalchemy import (Table, MetaData, create_engine, Column, Integer,
                        String, UniqueConstraint, Index)
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import sessionmaker, registry, declarative_base
engine = create_engine("sqlite:///pythonsql.db")

Session = sessionmaker(bind=engine)
session = Session()
mapper_registry = registry()
metadata = MetaData()

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


# Создание таблицы классическим способом
mapper_registry.map_imperatively(User, users)
metadata.create_all(bind=engine)

# Декларативный подход создания таблиц в БД
Base = declarative_base()

class Animal(Base):
    __tablename__ = "animals"
    # Index - добавляет индекс, UniqueConstraint - проверяет на уникальность
    __table_args__ = (Index("name_index", "name"), UniqueConstraint("name"))
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return f"Name: {self.name} Age: {self.age}"

# Создание таблицы используя декларативный подход
Base.metadata.create_all(bind=engine)