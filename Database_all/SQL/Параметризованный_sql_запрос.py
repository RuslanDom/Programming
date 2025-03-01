import sqlite3


class Fruits:
    def __init__(self, name:str, amount:int, price:float):
        self.name = name
        self.amount = amount
        self.price = price

    @staticmethod
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


def connect_db():
    with sqlite3.connect("test.db") as conn:
        return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    amount INTEGER NOT NULL CHECK (amount >= 0),
    price FLOAT NOT NULL CHECK (price > 0)
    );"""
    cursor.execute(sql)
    conn.commit()

def add_product() -> Fruits:
    while True:
        try:
            _name = input("Введите название фрукта:\n>>")
            _amount = int((input("Введите имеющиеся кол-во (кг):\n>>")))
            _price = float(input("Введите стоимость одного кг:\n>>>"))
            return Fruits(name=_name, amount=_amount, price=_price)
        except ValueError:
            print("Не верно указанны поля. Попробуйте ещё раз.")


def insert_product(n, a, p) -> None:
    conn = connect_db()
    cursor = conn.cursor()
    # НЕБЕЗОПАСНЫЙ ЗАПРОС INSERT
    # sql = f"INSERT INTO products (name, amount, price) VALUES('{n}', {a}, {p});"
    # cursor.execute(sql)

    # БЕЗОПАСНЫЙ ЗАПРОС
    sql = "INSERT INTO products (name, amount, price) VALUES (?, ?, ?)"
    cursor.execute(sql, (n, a, p))
    conn.commit()




if __name__ == '__main__':
    # create_table()  # Создание таблицы
    fruit = add_product()
    insert_product(fruit.name, fruit.amount, fruit.price)  # Вставка записи
    # Fruits.del_last_note("products") # Удаление last записи
    print(Fruits.get_table(table_name="products"))  # Получение данных таблицы