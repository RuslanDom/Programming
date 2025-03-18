import sqlite3
from typing import List
from wtforms.validators import InputRequired
from wtforms import StringField
from flask_wtf import FlaskForm

DATA = [
    {'id': 0, 'title': 'A Byte of Python', 'author': 'Swaroop C.H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 3, 'title': 'War and Piece', 'author': 'Lev Tolstoy'}
]

class Book:
    # title = StringField(validators=[InputRequired(message="Не заполнено поле название")])
    # author = StringField(validators=[InputRequired(message="Не заполнено поле имя автора")])
    def __init__(self, id:int, title:str, author:str) -> None:
        self.id = id
        self.title = title
        self.author = author

    # Позволяет обращаться к элементам объекта через [] скобки как в словаре
    # Этот метод помогает поддерживать обратную совместимость
    def __getitem__(self, item):
        return getattr(self, item)



def init_db(initial_records: List[dict]):
    with sqlite3.connect('table_books.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='table_books';")
        exists = cursor.fetchone()
        if not exists:
            cursor.executescript("""CREATE TABLE 'table_books' 
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT);""")

            cursor.executemany("""INSERT INTO table_books (title, author) VALUES (?, ?);""",
                               [(item['title'], item['author']) for item in initial_records])


def get_all_books():
    with sqlite3.connect('table_books.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM table_books;")
        all_books = cursor.fetchall()
        return [Book(*row) for row in all_books]

def set_book(title, author):
    with sqlite3.connect('table_books.db') as connection:
        cursor = connection.cursor()
        sql_insert = """
        INSERT INTO table_books (title, author) VALUES (?, ?);
        """
        cursor.execute(sql_insert, (title, author))
        connection.commit()



# if __name__ == '__main__':
#     init_db(DATA)