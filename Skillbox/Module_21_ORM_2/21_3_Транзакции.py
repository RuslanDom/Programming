from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

engine = create_engine("sqlite:///:memory:", echo=True)
Session = sessionmaker(bind=engine, autoflush=True)  # autoflash - сохраняет в кэш действия с сессией до коммита
session = Session()
Base = declarative_base()

# Точка сохранения (создание транзакции и точки для отката)
# with session.begin():
#     session.add_all([first_obj(), second_obj()])
#     nested_transaction = session.begin_nested()
#     session.add(third_obj)
#     nested_transaction.rollback()

class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    children = relationship("Child", backref="parent")

    def __repr__(self):
        return f"Parent name={self.name}"


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('parent.id'))

    def repr(self):
        return f"Child name={self.name}, parent_id={self.parent_id}"



if __name__ == "__main__":
    Base.metadata.create_all(engine)

    parent = Parent(name="Daddy")
    session.add(parent)

    q1 = session.query(Parent).all()
    print(q1)
    session.commit()

    new_session = Session()
    new_session.autoflush = False

    new_session.add(Parent(name="Father"))
    q_2 = session.query(Parent).all()
    print(q_2)






