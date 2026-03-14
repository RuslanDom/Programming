from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import ForeignKey, String, Integer

class Base(DeclarativeBase):
    pass


class Human(Base):
    __tablename__ = 'Humans'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] = mapped_column(Integer())


DB_URL = 'sqlite:///db/database.db'

engine = create_engine(url=DB_URL, echo=True)
# echo - включает логгирование событий БД

def create_db_and_tables() -> None:
    # Создаёт таблицы, на основе объявленных моделей
    Base.metadata.create_all(engine)


Session = sessionmaker(engine)

joe = Human(name="Joe", age=33)

def create_human(human: Human, session):
    session.add(human)


with Session() as session:
    try:
        create_human(joe, session)
    except:
        session.rollback()
        raise
    else:
        session.commit()
