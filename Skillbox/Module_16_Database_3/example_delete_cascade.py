import sqlite3

DATABASE = "hw_16.db"
ENABLE_FOREIGN_KEYS = "PRAGMA foreign_keys = ON;"





def init_authors():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50)
            );
            """
        )
        conn.commit()



def init_books():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(50),
            author VARCHAR(50),
            FOREIGN KEY (author) REFERENCES authors(id) ON DELETE CASCADE
            );
            """
        )
        conn.commit()


def add_book(title, author):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO books (title, author) VALUES (?, ?)
            """,
            (title, author)
        )
        conn.commit()


def add_author(author):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO authors (name) VALUES (?)
            """,
            (author,)
        )
        conn.commit()


def delete_author(id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(ENABLE_FOREIGN_KEYS)
        cursor.execute(
            """
            DELETE FROM authors WHERE id = ?
            """,
            (id,)
        )
        conn.commit()

def get_id(name):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id FROM authors WHERE name = ?
            """,
            (name,)
        )
        return cursor.fetchone()[0]

def add_data():
    names = [
        "Stan",
        "Stiv",
        "John"
    ]
    titles = [
        "Black",
        "Red",
        "Green"
    ]
    for name, title in zip(names, titles):
        add_author(name)
        author_id = get_id(name)
        add_book(title=title, author=author_id)

if __name__ == "__main__":
    init_authors()
    init_books()
    # add_data()
    delete_author(1)




