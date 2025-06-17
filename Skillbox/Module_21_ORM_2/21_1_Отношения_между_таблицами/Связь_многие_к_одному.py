from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()
engine = create_engine("sqlite:///db_folder/many_to_one.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    child_id = Column(Integer, ForeignKey("child.id"))
    child = relationship("Child", backref="parent")

    def __repr__(self):
        return f"Parent(name: {self.name}, child_id: {self.child_id})"

class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Child(name: {self.name})"

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    parent_1 = Parent(name="Dad", child_id=1)
    parent_2 = Parent(name="Mom", child_id=1)
    child = Child(name="son")
    session.add(parent_1)
    session.add(parent_2)
    session.add(child)
    session.commit()
    parents = session.query(Parent).all()
    child = session.query(Child).first()
    print(parents)
    print(child)
