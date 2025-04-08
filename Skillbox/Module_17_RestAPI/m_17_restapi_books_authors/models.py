import sqlite3
from dataclasses import dataclass
from typing import Optional, Union, List, Dict


DATA = [
    {'id': 0, 'title': 'A Byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 3, 'title': 'War and Peace', 'author': 'Leo Tolstoy'},
]

ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON;"

DATABASE_NAME = 'table_books'
BOOKS_TABLE_NAME = 'books'


@dataclass
class Book:
    title: str = None
    author: str = None
    id: Optional[int] = None

    def __getitem__(self, item: str) -> Union[int, str]:
        return getattr(self, item)

@dataclass
class Author:
    first_name: str = None
    last_name: str = None
    middle_name: str = None
    id: Optional[int] = None

    def __getitem__(self, item: str) -> Union[int, str]:
        return getattr(self, item)


def init_author_table(initial_records: List[Dict]) -> None:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='authors_table'
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(
                f"""
                CREATE TABLE authors_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                middle_name VARCHAR(50) DEFAULT None
                );
                """
            )
            conn.commit()
            for item in initial_records:
                author_obj = refactoring_author_name(item['author'])
                add_author(author_obj)


def refactoring_author_name(data_name: str) -> dict:
    author: list = [item for item in data_name.split()]
    if len(author) > 2:
        author_dict = {"first_name": author[0], "last_name": author[1], "middle_name": author[2]}
    elif len(author) == 2:
        author_dict = {"first_name": author[0], "last_name": author[1], "middle_name": "UNKNOWN"}
    else:
        raise ValueError("Неправильно указаны данные")
    return author_dict


def add_author(author: dict or Author) -> Author:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        if isinstance(author, Author):
            if author.middle_name is None:
                author.middle_name = "UNKNOWN"
            cursor.execute(
                """
                INSERT INTO authors_table (first_name, last_name, middle_name)
                VALUES (?, ?, ?)
                """,
                (author.first_name, author.last_name, author.middle_name)
            )
        else:
            if author['middle_name'] is None:
                author['middle_name'] = "UNKNOWN"
            cursor.execute(
                """
                INSERT INTO authors_table (first_name, last_name, middle_name)
                VALUES (?, ?, ?)
                """,
                (author["first_name"], author["last_name"], author["middle_name"])
            )
        conn.commit()
        author_id = cursor.lastrowid
        return get_author_by_id(cursor, author_id)


def init_db(initial_records: List[Dict]) -> None:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='{BOOKS_TABLE_NAME}';
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(
                f"""
                CREATE TABLE `{BOOKS_TABLE_NAME}`(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    title TEXT NOT NULL, 
                    author VARCHAR(50) NOT NULL,
                    FOREIGN KEY (author) REFERENCES authors_table(id) ON DELETE CASCADE
                );
                """
            )
            conn.commit()
            for item in initial_records:
                book = Book(**item)
                add_book(book)


def _get_book_obj_from_row(row: tuple) -> Book:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM authors_table WHERE id=?
            """,
            (row[2],),
        )
        author = cursor.fetchone()
    return Book(id=row[0], title=row[1], author=Author(id=author[0],
                                                       first_name=author[1],
                                                       middle_name=author[3],
                                                       last_name=author[2]))


def add_book(book: Book) -> Book:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        if type(book.author) is str :
            author_id = get_author_id_use_name(cursor, book.author)[0]
        else:
            author_id = book.author
        cursor.execute(
            f"""
            INSERT INTO `{BOOKS_TABLE_NAME}`
            (title, author) VALUES (?, ?)
            """,
            (book.title, author_id)
        )
        conn.commit()
        data_id = cursor.lastrowid
        return get_book_by_id(data_id)


def get_all_books() -> list[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM `{BOOKS_TABLE_NAME}`')
        all_books = cursor.fetchall()
        return [_get_book_obj_from_row(row) for row in all_books]


def get_book_by_id(book_id: int) -> Optional[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM `{BOOKS_TABLE_NAME}` WHERE id = ?
            """,
            (book_id,)
        )
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)


def update_book_by_id(book: Book, id):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM `{BOOKS_TABLE_NAME}` WHERE id = ?
            """,
            (id,)
        )
        data = cursor.fetchone()
        if data:
            cursor.execute(
                f"""
                UPDATE '{BOOKS_TABLE_NAME}'
                SET title = ?, author = ?
                WHERE id = ?
                """,
                (book.title, book.author, id)
            )
            conn.commit()
            res = _get_book_obj_from_row((id, book.title, book.author))
            return res


def patch_book(book: Book, id: int) -> Book or tuple[str, int]:
    data: Book = get_book_by_id(id)
    if data:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            if book.title:
                cursor.execute(
                    f"""
                    UPDATE '{BOOKS_TABLE_NAME}' SET title = ?
                    WHERE id = ?
                    """,
                    (book.title, id)
                )
            else:
                cursor.execute(
                    f"""
                    UPDATE '{BOOKS_TABLE_NAME}' SET author = ?
                    WHERE id = ?
                    """,
                    (book.author, id)
                )
            conn.commit()
            cursor.execute(
                f"""
                SELECT * FROM `{BOOKS_TABLE_NAME}` WHERE id = ?
                """,
                (id,)
            )
            res = _get_book_obj_from_row(cursor.fetchone())
            return res


def delete_book_by_id(book_id: int) -> tuple[str, int]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        data = gets_the_book_by_id(book_id)
        if data:
            cursor.execute(
                f"""
                DELETE FROM '{BOOKS_TABLE_NAME}'
                WHERE id = ?
                """,
                (book_id,)
            )
            conn.commit()
            return 'Success', 204
        else:
            return 'Error. This book is not found', 404


def get_book_by_title(book_title: str) -> Optional[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{BOOKS_TABLE_NAME}' WHERE title = ?
            """,
            (book_title,)
        )
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)


def gets_the_book_by_id(id: int) -> Optional[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{BOOKS_TABLE_NAME}' WHERE id = ?
            """, (id,)
        )
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)


def get_author_id_use_name(cursor: sqlite3.Cursor, author) -> int or None:
    author = tuple(author.split())
    cursor.execute(
        f"""
        SELECT id FROM authors_table WHERE last_name IN {author} AND first_name IN {author};
        """
    )
    result = cursor.fetchone()
    if result:
        return result



def get_author_by_id(cursor: sqlite3.Cursor, author_id: int) -> Author:
    cursor.execute(
        """
        SELECT * FROM authors_table WHERE id = ?
        """,
        (author_id,)
    )
    author = cursor.fetchone()
    return Author(id=author[0], first_name=author[1], last_name=author[2], middle_name=author[3])


def get_author_obj_from_row(row: tuple) -> Author:
    return Author(id = row[0], first_name=row[1], last_name=row[2], middle_name=row[3])


def get_all_authors():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM authors_table;
            """
        )
        authors = cursor.fetchall()
        return [get_author_obj_from_row(author) for author in authors]


def get_all_books_by_author_id(author_id: int) -> list[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{BOOKS_TABLE_NAME}' WHERE author = ?
            """,
            (author_id,)
        )
        books = cursor.fetchall()
        return [_get_book_obj_from_row(book) for book in books]


def delete_author_with_books(author_id: int):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(ENABLE_FOREIGN_KEY)
        cursor.execute(
            """
            SELECT id FROM authors_table WHERE id = ?
            """,
            (author_id,)
        )
        data = cursor.fetchone()
        if data:
            cursor.execute(
                f"""
                DELETE FROM authors_table WHERE id = ?                
                """,
                (author_id,)
            )
            conn.commit()
            return 'Success', 204
        else:
            return 'Error. This author is not found', 404