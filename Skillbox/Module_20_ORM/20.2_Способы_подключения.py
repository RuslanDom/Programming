from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


"""
Engine - определение
engine = 
create_engine("dialect[+driver]:///login:password@host/db_name[?key=value]")
где:
dialect - это название СУБД(mssql, postgres, mysql)
driver - это название DBAPI(psycopg2, pyodbc)
Пример:
engine = 
create_engine("mssql+pyodbc:///admin:qwerty@localhost/my_db")
"""
Base = declarative_base()



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    login = Column(String)

    def __repr__(self):
        return f"USER: id={self.id}, name={self.name}, email={self.email}, login={self.login}"

def first_part(engine):
    with engine.connect() as connection:
        create_user_table = """CREATE TABLE IF not EXISTS users (
        id integer PRIMARY KEY, 
        name text NOT NULL,
        email text,
        login text NOT NULL)"""
        connection.execute(text(create_user_table))

        # Текст запроса на вставку данных
        insert_q = """INSERT INTO users (name, email, login) VALUES ('Bogdan', 'bog@gmail.com', 'bogDOS')"""
        connection.execute(text(insert_q))
        # connection.commit()

        # Текст запроса на получение данных
        filter_query = text("SELECT * FROM users WHERE id=:r_id")  # =: Это параметр привязки
        # Параметр привязки используют для того чтобы в дальнейшем передать именованный параметр
        cursor = connection.execute(filter_query, dict(r_id=1))


        result = cursor.fetchone()
        print(result)

def second_part(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    some_object = User(name='ruslan', email='rus@gmail.com', login='Dad')
    try:
        # session.add(some_object)
        # session.commit()
        query = session.query(User).filter_by(name='ruslan').all()
        print(query)
    finally:
        session.close()


if __name__ == "__main__":
    engine = create_engine("sqlite:///pythonsql.db")
    # first_part(engine)
    second_part(engine)
