import sqlite3
from typing import Optional, List
from dataclasses import dataclass

DATA = [
    {'id': 0, 'title': 'A Byte of Python', 'author': 'Swaroop C.H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 3, 'title': 'War and Piece', 'author': 'Lev Tolstoy'}
]

BOOKS_TABLE_NAME = 'books'

@dataclass
class Book:
    title: str
    author: str
    id: Optional[int]

    def __getitem__(self, item):
        return getattr(self, item)


def init_db(initial_records: List[dict]):
    with sqlite3.connect('module_17.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='{BOOKS_TABLE_NAME}'
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(
                f"""
                CREATE TABLE {BOOKS_TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(50) NOT NULL,
                author VARCHAR(50) NOT NULL
                )
                """
            )


            cursor.executemany(
                f"""
                INSERT INTO {BOOKS_TABLE_NAME} (title, author)
                VALUES (?, ?)
                """, [(item['title'], item['author']) for item in initial_records]
            )

def get_book_obj_from_row(row) -> Book:
    return Book(id=row[0], title=row[1], author=row[2])

def get_all_records():
    with sqlite3.connect('module_17.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{BOOKS_TABLE_NAME}'
            """
        )
        all_books = cursor.fetchall()
        return [get_book_obj_from_row(row) for row in all_books]

def get_record_by_id(id: int) -> Optional[Book]:
    with sqlite3.connect('module_17.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{BOOKS_TABLE_NAME}'
            WHERE id=?
            """,
            (id,)
        )
        book = cursor.fetchone()
        if book:
            return get_book_obj_from_row(book)

def get_record_by_author(author: str) -> Optional[Book]:
    with sqlite3.connect('module_17.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                            SELECT * FROM '{BOOKS_TABLE_NAME}'
                            WHERE author=?""", (author,))
        book = cursor.fetchone()
        if book:
            return get_book_obj_from_row(book)

def add_record(book: Book) -> Book:
    with sqlite3.connect('module_17.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO {BOOKS_TABLE_NAME} (title, author)
            VALUES (?, ?)
            """,
            (book.title, book.author)
        )
        conn.commit()
        book.id = cursor.lastrowid
        return book

def update_record(book: Book):
    with sqlite3.connect('module_17.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE {BOOKS_TABLE_NAME}
            SET title = ?, author = ?
            WHERE id = ?
            """,
            (book.title, book.author, book.id)
        )
    conn.commit()

def delete_record(id):
    with sqlite3.connect('module_17.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM {BOOKS_TABLE_NAME}
            WHERE id = ?
            """,
            (id,)
        )
        conn.commit()








