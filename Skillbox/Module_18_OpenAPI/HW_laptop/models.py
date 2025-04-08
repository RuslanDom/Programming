import sqlite3
from typing import Optional, List, Dict
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
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    id: Optional[int] = None

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Book:
    title: str
    author: Optional[Author.id] = None
    id: Optional[int] = None

    def __getitem__(self, item):
        return getattr(self, item)


def init_authors_table(data):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master
            WHERE type = 'table' AND name = '{AUTHORS_TABLE_NAME}'
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(
                f"""
                CREATE TABLE '{AUTHORS_TABLE_NAME}'(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                middle_name VARCHAR(50)
                )
                """
            )
            for item in data:
                author = refactoring_author_name(item['author'])
                cursor.execute(
                    f"""
                    INSERT INTO '{AUTHORS_TABLE_NAME}'(first_name, last_name, middle_name)
                    VALUES (?, ?, ?)
                    """,
                    (author.first_name, author.last_name, author.middle_name)
                )
            conn.commit()


def init_books_table(data):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master
            WHERE type = 'table' AND name = '{BOOKS_TABLE_NAME}'
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(
                f"""
                CREATE TABLE '{BOOKS_TABLE_NAME}'(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(50) NOT NULL,
                author INTEGER NOT NULL,
                FOREIGN KEY (author) REFERENCES '{AUTHORS_TABLE_NAME}' (id) ON DELETE CASCADE
                )
                """
            )
            for item in data:
                cursor.execute(
                    f"""
                    SELECT id FROM '{AUTHORS_TABLE_NAME}'
                    WHERE last_name='{refactoring_author_name(item["author"]).last_name}'
                    """
                )
                item["author"] = cursor.fetchone()[0]
                cursor.execute(
                    f"""
                    INSERT INTO '{BOOKS_TABLE_NAME}'(title, author)
                    VALUES (?, ?)
                    """,
                    (item['title'], item['author'])
                )
            conn.commit()


# Получаем все книги в виде списка объектов Book
def get_all_books() -> List[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{BOOKS_TABLE_NAME}'
            """
        )
        books_list = cursor.fetchall()

    return [
        Book(
            id=book[0],
            title=book[1],
            author=book[2]
            )
        for book in books_list]

# Получаем объект Author с помощью id
def get_author_by_id(author_id) -> Optional[Author]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{AUTHORS_TABLE_NAME}'
            WHERE id = '{author_id}'
            """
        )
        author = cursor.fetchone()
        if author:
            return Author(id=author[0], first_name=author[1], last_name=author[2], middle_name=author[3])

# Получаем всех авторов в виде списка объектов Author
def get_all_authors() -> List[Author]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{AUTHORS_TABLE_NAME}'
            """
        )
        authors_list = cursor.fetchall()
        return [Author(
            id=authors[0],
            first_name=authors[1],
            last_name=authors[2],
            middle_name=authors[3]
        )
            for authors in authors_list]

# Добавление нового автора
def add_author(author_data: Author) -> Author:
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
        last_id = cursor.lastrowid
        added_author = get_author_by_id(last_id)
        return added_author

# Добавление новой книги
def add_book(book_data: Book) -> Book:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            INSERT INTO '{BOOKS_TABLE_NAME}'
            (title, author)
            VALUES (?, ?)
            """,
            (book_data.title, book_data.author)
        )
        conn.commit()
        last_id = cursor.lastrowid
        return get_book_by_id(last_id)

# Получение книги по ID
def get_book_by_id(id: int) -> Optional[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{BOOKS_TABLE_NAME}'
            WHERE id = '{id}'
            """
        )
        exists_book: tuple[int, str] = cursor.fetchone()
        if exists_book:
            return Book(
                id=exists_book[0],
                title=exists_book[1],
                author=exists_book[2]
            )

# Получение всех книг относящихся к автору
def get_all_books_by_author_id(author_id: int) -> List[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{BOOKS_TABLE_NAME}'
            WHERE author = '{author_id}'
            """
        )
        books_list = cursor.fetchall()
        return [Book(id=book[0], title=book[1], author=book[2]) for book in books_list]

# Обновление update данных книги по ID
def put_updated_book(book: Book, id: int) -> Book:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            UPDATE '{BOOKS_TABLE_NAME}' 
            SET title = ?, author = ?
            WHERE id = ?
            """,
            (book.title, book.author, id)
        )
        conn.commit()
    return get_book_by_id(id)

# Обновление частичное(patch), автора или названия книги
def patch_book(book: Book, id: int) -> Book:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        # Обновление только названия книги
        if book.title:
            cursor.execute(
                f"""
                UPDATE '{BOOKS_TABLE_NAME}' 
                SET title = ?
                WHERE id = ?
                """,
                (book.title, id)
            )
        # Обновление только автора
        elif book.author:
            # Проверка на существование автора в БД
            existing_author = get_author_by_last_name(refactoring_author_name(book.author).last_name)
            if existing_author:
                # Если автор существует, получаем его ID
                author_id: int = get_author_by_last_name(refactoring_author_name(book.author).last_name).id
            else:
                # Если автора нет, добавляем его в БД и получаем его ID
                author_id: int = add_author(refactoring_author_name(book.author)).id

            cursor.execute(
                f"""
                UPDATE '{BOOKS_TABLE_NAME}' 
                SET author = ?
                WHERE id = ?
                """,
                (author_id, id)
            )
        conn.commit()
    return get_book_by_id(id)

# Удаление книги по ID
def delete_book(id: int) -> Optional[dict]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{BOOKS_TABLE_NAME}'
            WHERE id = ?
            """,
            (id,)
        )
        if cursor.fetchone():
            cursor.execute(
                f"""
                DELETE FROM '{BOOKS_TABLE_NAME}'
                WHERE id = ?
                """,
            (id,)
            )
            conn.commit()
            return None
        return {"error": "book not found"}

# Удаление автора по ID
def delete_author(id: int) -> Optional[dict]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{AUTHORS_TABLE_NAME}'
            WHERE id = ?
            """,
            (id,)
        )
        if cursor.fetchone():
            cursor.execute(
                f"""
                DELETE FROM '{AUTHORS_TABLE_NAME}'
                WHERE id = ?
                """,
                (id,)
            )
            conn.commit()
            return None
        return {"error": "author not found"}


# UTILS
def refactoring_author_name(data_name: str) -> Author:
    author_data: list = [item for item in data_name.split()]
    if len(author_data) > 2:
        author = Author(first_name=author_data[0], middle_name=author_data[1], last_name=author_data[2])
    elif len(author_data) == 2:
        author= Author(first_name=author_data[0], last_name=author_data[1], middle_name="UNKNOWN")
    else:
        raise ValueError("Неправильно указаны данные")
    return author


def get_author_by_last_name(name: str) -> Optional[Author]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{AUTHORS_TABLE_NAME}'
            WHERE last_name = '{name}';
            """
        )
        author: tuple[int, str] = cursor.fetchone()
        if author:
            return Author(
                id=author[0],
                first_name=author[1],
                last_name=author[2],
                middle_name=author[3]
            )


def get_book_by_title(title: str) -> Optional[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{BOOKS_TABLE_NAME}'
            WHERE title='{title}'
            """
        )
        exists_book: tuple[int, str] = cursor.fetchone()
        if exists_book:
            return Book(
                id=exists_book[0],  # ID книги (int)
                title=exists_book[1],  # Название книги (str)
                author=exists_book[2]  # int
            )


def exists_author(data_author: Author) -> int:
    exists = get_author_by_last_name(data_author.last_name)
    if exists:
        author = exists.id
    else:
        author = add_author(data_author).id
    return author