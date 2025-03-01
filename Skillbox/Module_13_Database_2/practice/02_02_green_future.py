import sqlite3



def get_number_of_lucky_days(cursor: sqlite3.Cursor, month_number: int) -> float:
    pattern = fr'2024-{month_number}-__'
    sql = f"""
        SELECT * FROM table_green_future
        WHERE date LIKE '{pattern}' AND 
            action IN ('мешок пластика', 'мешок алюминия', 'отнесли мешки на завод');
    """
    sql_request_all_month_days = f"""
    SELECT date FROM table_green_future
    WHERE date LIKE '{pattern}'
    GROUP BY date;
"""
    cursor.execute(sql)
    result_request = cursor.fetchall()
    cursor.execute(sql_request_all_month_days)
    count_days = cursor.fetchall()
    lucky_days = dict()
    for day in result_request:
        if lucky_days.setdefault(day[1]):
            lucky_days[day[1]] += [day[2]]
        else:
            lucky_days[day[1]] =[day[2]]
    result = 0
    for key, value in lucky_days.items():
        if len(value) == 4:
            result += 1
    return result * 100 / len(count_days)


if __name__ == "__main__":
    with sqlite3.connect("practise.db") as conn:
        cursor = conn.cursor()
        percent_of_lucky_days = get_number_of_lucky_days(cursor, 12)
        print(percent_of_lucky_days)
        print(f"В декабре у ребят было {percent_of_lucky_days:.02f}% удачных дня!")
