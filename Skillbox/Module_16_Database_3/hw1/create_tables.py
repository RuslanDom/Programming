import sqlite3

ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON;"

with open("requests.sql", "r") as file:
    requests = file.read()

with sqlite3.connect("../hw_16.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(requests)
    connection.commit()