import sqlite3


ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys=ON;"

# Суррогатные primary_key(PK), когда PK ничего не означает просто столбец с цифрами
CREATE_USER_TABLE = """
    DROP TABLE IF EXISTS users;
    CREATE TABLE users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        first_name VARCHAR(255) NOT NULL
    );
    """

# ON DELETE CASCADE удалит всю запись, если её часть была удалена
CREATE_BRIDGE_BETWEEN_TABLE = """
DROP TABLE IF EXISTS likes;
CREATE TABLE likes(
    like_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES users (user_id) ON DELETE CASCADE,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts (post_id) ON DELETE CASCADE
);
"""




CREATE_POST_TABLE = """
    DROP TABLE IF EXISTS posts;
    CREATE TABLE posts(
        post_id INTEGER PRIMARY KEY AUTOINCREMENT,
        author VARCHAR(255) NOT NULL,
        content TEXT NOT NULL DEFAULT ''
    );
    """




# С использованием естественного ключа
CREATE_USER_NATURAL_TABLE = """
    DROP TABLE IF EXISTS users;
    CREATE TABLE users(
        username VARCHAR(255) NOT NULL PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        first_name VARCHAR(255) NOT NULL
    );
    """

# Композитный ключ
CREATE_BRIDGE_BETWEEN_TABLE_WITH_COMPOSITE_KEY = """
DROP TABLE IF EXISTS likes;
    CREATE TABLE likes(
        username INTEGER NOT NULL REFERENCES users(username) ON DELETE CASCADE,
        post_id INTEGER NOT NULL,
        FOREIGN KEY(post_id) REFERENCES posts(post_id) ON DELETE CASCADE
        PRIMARY KEY(username, post_id)
    );
    """

def create_tables():
    with sqlite3.connect("hw_16.db") as conn:
        cursor = conn.cursor()
        cursor.executescript(CREATE_USER_NATURAL_TABLE)
        cursor.executescript(CREATE_POST_TABLE)
        cursor.executescript(CREATE_BRIDGE_BETWEEN_TABLE_WITH_COMPOSITE_KEY)
        conn.commit()


if __name__ == "__main__":
    create_tables()

