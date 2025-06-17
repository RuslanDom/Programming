from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base


engine = create_engine("sqlite:///many_to_many.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Table(name, metadata, *args)
integration_table = Table(
    "integrations",
    Base.metadata,
    Column("parent_id", ForeignKey("parent.id"), primary_key=True),
    Column("child_id", ForeignKey("child.id"), primary_key=True),
)



class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    # children = relationship("Child", secondary=integration_table)

    # Двунаправленная связь
    children = relationship(
        "Child",
        secondary=integration_table,
        back_populates="parents"
    )

    # С помощью backref
    # children = relationship(
    #     "Child",
    #     secondary=integration_table,
    #     backref="parent"
    # )


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parents = relationship(
        "Parent",
        secondary=integration_table,
        back_populates="children"
    )


if __name__ == "__main__":
    Base.metadata.create_all(engine)