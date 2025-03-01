import sqlite3

def get_all_records(cursor: sqlite3.Cursor) -> None:
    sql = "SELECT COUNT(*) FROM table_kotlin"
    cursor.execute(sql)
    all_records, *_ = cursor.fetchone()
    print(f"Всего записей дней: {all_records}")

def get_storm_days(cursor: sqlite3.Cursor, power_wind: int):
    sql_request = f"""
            SELECT COUNT(*)
            FROM table_kotlin
            WHERE wind >= ?;
        """
    cursor.execute(sql_request, (power_wind, ))
    res, *_ = cursor.fetchone()
    return res


if __name__ == "__main__":
    power = 40
    with sqlite3.connect('practise.db') as connection:
        cursor = connection.cursor()
        result = get_storm_days(cursor, power)
        print(f"Всего штормовых дней с силой ветра выше {power}: {result}")