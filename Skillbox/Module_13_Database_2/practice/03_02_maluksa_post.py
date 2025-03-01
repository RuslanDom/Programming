# Вы программист в почтовом отделении деревни Малукса. Известно, что ваша деревня весьма удалена от других
# населённых пунктов и дорогу к ней иногда размывает. Сейчас май, и дорогу опять размыло!
# Нужно написать SQL-скрипт, который перенесёт все почтовые отправления с мая на июнь,
# так как в июне дорога просохнет.

import sqlite3
pattern = r"__-05-____"
sql_select = f"""SELECT * FROM table_russian_post_2 WHERE order_day LIKE '{pattern}';"""

if __name__ == "__main__":
    with sqlite3.connect("practise.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql_select)
        res = cursor.fetchall()
        result = []
        for row in res:
            row = list(row)
            row[1] = row[1].replace('05', '06')
            row = tuple(row)
            result.append(row)
        for row in result:
            sql_script_to_execute = (f"""UPDATE table_russian_post_2
                                         SET order_day = '{row[1]}'
                                         WHERE order_id = {row[0]};""")
            cursor.execute(sql_script_to_execute)

        conn.commit()
