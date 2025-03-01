import sqlite3


def add_books_from_file(cursor: sqlite3.Cursor, file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    lines = list(map(lambda line: line.split(","), lines[1:]))
    for line in lines:
        sql = """INSERT INTO table_books (book_name, author, publish_year, ISBN) VALUES (?, ?, ?, ?);"""
        cursor.execute(sql, (line[1], line[2], line[3], line[0]))



if __name__ == "__main__":
    with sqlite3.connect("practise.db") as conn:
        cursor = conn.cursor()
        add_books_from_file(cursor, "book_list.csv")
        conn.commit()
