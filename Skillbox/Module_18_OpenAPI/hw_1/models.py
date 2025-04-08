import sqlite3
from typing import Optional
from dataclasses import dataclass

DATA = [
    {'id': 0, 'title': 'A Byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 3, 'title': 'War and Peace', 'author': 'Leo Tolstoy'},
]
ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON;"
DATABASE_NAME = 'table_books'
BOOKS_TABLE_NAME = 'books'
AUTHORS_TABLE_NAME = 'authors'


@dataclass
class Author:
    id: int = None
    first_name: str = None
    last_name: str = None
    middle_name: Optional[str] = "UNKNOWN"


@dataclass
class Book:
    id: int = None
    title: str = None
    author: int = None


def init_author_table(initial_data):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master
            WHERE type = 'table' AND name = '{AUTHORS_TABLE_NAME}';
            """
        )
        exists = cursor.fetchone()
        if exists is None:
            cursor.execute(
                f"""
                CREATE TABLE '{AUTHORS_TABLE_NAME}' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                middle_name VARCHAR(50)
                )
                """
            )
            for item in initial_data:
                author: Author = refactoring_author_name(item["author"])
                cursor.execute(
                    f"""
                    INSERT INTO '{AUTHORS_TABLE_NAME}' (
                    first_name, last_name, middle_name)
                    VALUES (?, ?, ?)
                    """,
                    (author.first_name, author.last_name, author.middle_name)
                )
            conn.commit()


def init_book_table(initial_data):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master
            WHERE type = 'table' AND name = '{BOOKS_TABLE_NAME}';
            """
        )
        exists = cursor.fetchone()
        if exists is None:
            cursor.execute(
                f"""
                CREATE TABLE '{BOOKS_TABLE_NAME}' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(50) NOT NULL,
                author INTEGER NOT NULL,
                FOREIGN KEY (author) REFERENCES '{AUTHORS_TABLE_NAME}'(id) ON DELETE CASCADE
                )
                """
            )
            for item in initial_data:
                item["author"] = get_author_by_name(refactoring_author_name(item["author"]).last_name).id
                cursor.execute(
                    f"""
                    INSERT INTO '{BOOKS_TABLE_NAME}' 
                    (title, author)
                    VALUES (?, ?)
                    """,
                    (item["title"], item["author"])
                )
            conn.commit()

# Получение всех объектов книг и авторов
def get_all_authors():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{AUTHORS_TABLE_NAME}'
            """
        )
        authors_list = cursor.fetchall()
    return [_get_author_obj_by_row(author) for author in authors_list]

def get_all_books():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{BOOKS_TABLE_NAME}'
            """
        )
        books_list = cursor.fetchall()
    return [_get_book_obj_by_row(book) for book in books_list]


def add_author(author_data: Author):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            INSERT INTO '{AUTHORS_TABLE_NAME}' 
            (first_name, last_name, middle_name)
            VALUES (?, ?, ?)
            """,
            (author_data.first_name, author_data.last_name, author_data.middle_name)
        )
        conn.commit()
        author_id = cursor.lastrowid
        return get_author_by_id(author_id)



def get_author_by_id(id: int):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{AUTHORS_TABLE_NAME}'
            WHERE id = '{id}'
            """
        )
        exists = cursor.fetchone()
        if exists:
            return _get_author_obj_by_row(exists)


# UTILS
def refactoring_author_name(data_name: str) -> Author:
    author_data: list = [item for item in data_name.split()]
    if len(author_data) > 2:
        author= Author(first_name=author_data[0], last_name=author_data[1], middle_name=author_data[2])
    elif len(author_data) == 2:
        author = Author(first_name=author_data[0], last_name=author_data[1], middle_name="UNKNOWN")
    else:
        raise ValueError("Неправильно указаны данные")
    return author


def get_author_by_name(data_name: str) -> Optional[Author]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{AUTHORS_TABLE_NAME}'
            WHERE last_name = '{data_name}'
            """
        )
        exists = cursor.fetchone()
        if exists:
            return _get_author_obj_by_row(exists)


def get_book_by_title(title: str) -> Optional[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{BOOKS_TABLE_NAME}'
            WHERE title = '{title}'
            """
        )
        exists = cursor.fetchone()
        if exists:
            return _get_book_obj_by_row(exists)



# Получение объектов с кортежа(tuple)
def _get_book_obj_by_row(row: tuple) -> Book:
    return Book(id=row[0], title=row[1], author=row[2])

def _get_author_obj_by_row(row: tuple) -> Author:
    return Author(id=row[0], first_name=row[1], last_name=row[2], middle_name=row[3])



