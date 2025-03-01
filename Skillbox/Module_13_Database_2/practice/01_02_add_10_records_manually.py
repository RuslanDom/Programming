import sqlite3
import random
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

VEGETABLE = [
    "помидоры",
    "перец",
    "капуста",
    "баклажаны",
    "кабачки"
]

DESCRIPTION = [
    "солёные",
    "сушёные",
    "печёные",
    "варёные",
    "жареные",
]



def add_10_records_to_table_warehouse(cursor: sqlite3.Cursor) -> None:
    for _ in range(10):
        vegetable = random.choice(VEGETABLE)
        description = random.choice(DESCRIPTION)
        amount_val = random.randint(100, 10000)
        sql = """INSERT INTO table_warehouse (name, description, amount) VALUES (?, ?, ?)"""
        cursor.execute(sql, (vegetable, description, amount_val))



if __name__ == "__main__":
    with sqlite3.connect("practise.db") as conn:
        cursor = conn.cursor()
        add_10_records_to_table_warehouse(cursor)
        conn.commit()
