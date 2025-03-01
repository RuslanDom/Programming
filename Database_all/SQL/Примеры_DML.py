# DATA MANIPULATION LANGUAGE DML
import sqlite3


# INSERT
def insert():
    with sqlite3.connect('test.db') as conn:
        cursor = conn.cursor()
        sql_request = ("INSERT INTO products (name, amount, price) "
                       "VALUES (?, ?, ?);")
        cursor.execute(sql_request, ('кокос', 30, 188))
        conn.commit()


# SELECT
def select():
    with sqlite3.connect('test.db') as conn:
        cursor = conn.cursor()

        # Получить все записи таблицы
        sql_all = "SELECT * FROM products;"
        cursor.execute(sql_all)
        all_data = cursor.fetchall()
        print(all_data)

        # Получить запись с именем 'Лимон'
        sql_last_id = "SELECT * FROM products WHERE name LIKE 'Лимон';"
        cursor.execute(sql_last_id)
        last_id = cursor.fetchall()
        print(last_id)

        # Получить 5 записей от фильтрованных от большего к меньшему по цене с кол-вом amount > 10
        sql_request = ("SELECT * FROM products "
                       "WHERE amount > ? "
                       "ORDER BY price DESC LIMIT 5;")
        cursor.execute(sql_request, (10, ))
        result = cursor.fetchall()
        print(result)


# DELETE
def delete():
    with sqlite3.connect('test.db') as conn:
        cursor = conn.cursor()
        sql_request = ("DELETE FROM products "
                       "WHERE id IN (SELECT max(id) FROM products);")
        cursor.execute(sql_request)
        conn.commit()


# UPDATE
def update(delta_amount):
    with sqlite3.connect('test.db') as conn:
        cursor = conn.cursor()
        # Получение имя фрукта и его кол-во имеющего самое низкий amount(кол-во на складе)
        sql_for_update = ("SELECT name, amount FROM products "
                          "WHERE amount IN (SELECT min(amount) FROM products);")
        cursor.execute(sql_for_update)
        get_name, get_amount = cursor.fetchone()
        print(get_name, get_amount)
        new_amount = delta_amount + get_amount

        # Изменение кол-ва заданного фрукта UPDATE
        sql_request = ("UPDATE products "
                       "SET amount = ? WHERE name = ?;")
        cursor.execute(sql_request, (new_amount, get_name))
        conn.commit()



if __name__ == '__main__':
    # insert()
    # delete()
    update(delta_amount=1)
    print("Обновлённые данные")
    select()