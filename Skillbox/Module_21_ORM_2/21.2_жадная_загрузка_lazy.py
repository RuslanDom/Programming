from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, joinedload

engine = create_engine("sqlite:///:memory:", echo=True)
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
        back_populates="parents",
        lazy="select", # Ленивая загрузка подгружает данные из связанных дочерних таблиц по мере запроса к ним
        # lazy="joined" - Тип жадной загрузки сразу подгружает все связанные данные
        # lazy="subquery" - Второй тип жадной загрузки
        # lazy="selectin" - Третий тип жадной загрузки
        # lazy="no loader" - Отсутствие загрузки связанных данных
        # lazy="raise" - Отсутствие загрузки с выводом ошибки
    )

    def __repr__(self):
        return f"name: {self.name}, children: {self.children}"

class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("parent.id"))
    parents = relationship("Parent",secondary=integration_table, back_populates="children")

    def __repr__(self):
        return f"name: {self.name}, parents: {self.parents}"

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    parent = Parent(name="Father")
    child_1 = Child(name="Son", parent_id=1)
    child_2 = Child(name="Daughter", parent_id=1)
    session.add(parent)
    session.add(child_1)
    session.add(child_2)
    session.commit()

    print("REQUEST PARENT")
    my_parent = session.query(Parent).first()

    print()
    print("REQUEST CHILDREN")
    my_children = session.query(Child).all()
    for c in my_children:
        print(c.name)

    print()
    print("CUSTOM LAZY")
    q = session.query(Parent).options(joinedload(Parent.children)).all()

    print("END")