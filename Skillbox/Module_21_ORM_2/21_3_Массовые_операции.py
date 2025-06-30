from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from typing import List

engine = create_engine("sqlite:///:memory:", echo=True)
Session = sessionmaker(bind=engine, autoflush=True)
session = Session()
Base = declarative_base()


class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


    def __repr__(self):
        return f"Parent name: {self.name}"



if __name__ == '__main__':
    Base.metadata.create_all(engine)

    # bulk_save_objects - массово вставляет и если такие записи есть обновляет(insert, upload)
    parent_1 = Parent(name="Parent 1")
    parent_2 = Parent(name="Parent 2")
    parent_3 = Parent(name="Parent 3")
    parent_4 = Parent(name="Parent 4")

    session.bulk_save_objects([parent_1, parent_2, parent_3, parent_4])
    session.commit()

    parents = session.query(Parent).all()
    print(parents)

    # bulk_insert_mappings - массово добавляет новые записи в БД (insert)
    insert_parents: List[dict] = [
        {"name": "Dad_1"},
        {"name": "Dad_2"},
        {"name": "Dad_3"},
        {"name": "Dad_4"}
    ]

    session.bulk_insert_mappings(Parent, insert_parents)
    session.commit()

    parents = session.query(Parent).all()
    print(parents)

    # bulk_update_mappings - массово обновляет старые записи на новые в БД

    update_parents: List[dict] = [
        {"id": 1, "name": "Mom_1"},
        {"id": 2, "name": "Mom_2"},
        {"id": 3, "name": "Mom_3"},
        {"id": 4, "name": "Mom_4"}
    ]

    session.bulk_update_mappings(Parent, update_parents)
    session.commit()

    parents = session.query(Parent).all()
    print(parents)



















