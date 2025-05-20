from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

def first_part():
    with engine.connect() as connection:
        create_user_table = """CREATE TABLE IF not EXISTS users (
        id integer PRIMARY KEY, 
        name text NOT NULL,
        email text,
        login text NOT NULL)"""
        connection.execute(text(create_user_table))

        insert_q = """INSERT INTO users (name, email, login) VALUES ('Bogdan', 'bog@gmail.com', 'bogDOS')"""
        connection.execute(text(insert_q))
        # connection.commit()

        filter_query = text("SELECT * FROM users WHERE id=:r_id")
        cursor = connection.execute(filter_query, dict(r_id=1))


        result = cursor.fetchone()
        print(result)


if __name__ == "__main__":
    engine = create_engine("sqlite:///pythonsql.db")
    first_part()

