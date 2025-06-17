from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine("sqlite:///:memory:", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

integration_table = Table(
    "integration_table",
    Base.metadata,
    Column("parent_id", Integer, ForeignKey("parent.id"), primary_key=True),
    Column("child_id", Integer, ForeignKey("child.id"), primary_key=True),
)

class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    children = relationship(
        "Child",
        secondary=integration_table,
        back_populates="parents"
    )

    def __repr__(self):
        return f"name: {self.name}, children: {self.children}"

class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # parent_id = Column(Integer, ForeignKey("parent.id"))

    parents = relationship("Parent",secondary=integration_table, back_populates="children")

    def __repr__(self):
        return f"name: {self.name}, parents: {self.parents}"

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    father = Parent(name="Father")
    mother = Parent(name="Mother")

    son = Child(name="Son")
    daughter = Child(name="Daughter")

    # Добавление отцу детей
    # children - коллекция детей
    father.children.extend([son, daughter])

    # Обратная ситуация, добавление сыну и дочери, маму
    son.parents.append(mother)
    daughter.parents.append(mother)

    session.add(father)
    session.add(mother)
    session.add(son)
    session.add(daughter)
    session.commit()

    my_parents = session.query(Parent).all()
    my_children = session.query(Child).all()
    print(my_parents)
    print(my_children)
    many_to_many_data = session.query(integration_table).all()

    # father.children.remove(daughter)
