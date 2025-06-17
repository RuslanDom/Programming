from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base


engine = create_engine("sqlite:///db_folder/one_to_one.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # backref
    child = relationship("Child", backref="parent", uselist=False)

    # Использование back_populates
    # child = relationship("Child", back_populates="parent", uselist=False)

    def __repr__(self):
        return f"name: {self.name}"

class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("parent.id"), unique=True)

    # Использование back_populates
    # parent = relationship("Parent", back_populates="child", uselist=False)

    def __repr__(self):
        return f"name: {self.name}, parent_id: {self.parent_id}"

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    parent = Parent(name="parent")
    session.add(parent)
    session.commit()

    child_one = Child(name="child_one", parent_id=1)
    session.add(child_one)
    session.commit()

    # check parent
    check_parent = session.query(Parent).filter_by(id=1).one()
    print(check_parent)

    # check child
    check_children = session.query(Child).all()
    print(check_children)
