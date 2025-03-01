import sqlite3

class Products:
    def __init__(self, name:str, description:str, amount:int) -> None:
        self.name = name
        self.description = description
        self.amount = amount

    def get_table(table_name):
        conn = connect_db()
        cursor = conn.cursor()
        sql = f"SELECT * FROM {table_name} ORDER BY id DESC LIMIT 5;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @staticmethod
    def del_last_note(table_name):
        conn = connect_db()
        cursor = conn.cursor()
        # Удаление последней созданной записи в БД максимальное id
        sql = f"DELETE FROM {table_name} WHERE id in (SELECT max(id) FROM {table_name});"
        cursor.execute(sql)
        conn.commit()

def add_new_product() -> Products:
    while True:
        name = input("Enter product name: ")
        description = input("Enter product description: ")
        try:
            amount = int(input("Enter product amount: "))
            return Products(name=name, description=description, amount=amount)
        except ValueError:
            print("Invalid amount. Try again")

def connect_db():
    with sqlite3.connect("module13.db") as conn:
        return conn


def create_table():
    db = connect_db()
    cursor = db.cursor()
    sql = """
            CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100),
            description TEXT,
            amount INTEGER CHECK (amount >= 0));"""
    cursor.execute(sql)
    db.commit()


def insert_product(name, description, amount):
    db = connect_db()
    cursor = db.cursor()
    sql = "INSERT INTO product (name, description, amount) VALUES (?, ?, ?);"
    cursor.execute(sql, (name, description, amount))
    db.commit()


def update_product(*args):
    db = connect_db()
    cursor = db.cursor()
    sql = "UPDATE product SET name = ? WHERE id == ?;"
    cursor.execute(sql, (args[1], args[0]))
    db.commit()


if __name__ == '__main__':
    # create_table()
    # insert_product("бананы", "Сладкий фрукт продолговатой формы, желтого цвета", 150)
    # update_product(1, "Бананы")
    new_product = add_new_product()
    insert_product(new_product.name, new_product.description, new_product.amount)