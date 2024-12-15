import sqlite3

# Чтобы подключиться к БД, используем метод connect:
conn = sqlite3.connect('../Skillbox/Telegram_bot/Trainer/database.db')
conn.close()

# Лучше предпочесть контекстный менеджер для корректного завершения работы в случае возникновения ошибок.
with sqlite3.connect('../Skillbox/Telegram_bot/Trainer/database.db') as conn:
    # Чтобы использовать SQL и получать результаты запросов, нужен курсор.
    # Это специальный объект, создаваемый методом cursor():
    cursor = conn.cursor()
    # INSERT INTO Добавить новую запись в БД
    # cursor.execute('INSERT INTO My_family (name, surname) VALUES ("Jerry", "Domashevskiy");')
    conn.commit()
    # Метод .execute исполняет переданный SQL-запрос.
    cursor.execute('SELECT * FROM My_family;')
    #  С помощью fetchall() мы можем получить все записи, который этот запрос нам вернул, в виде списка кортежей.
    print(cursor.fetchall())




