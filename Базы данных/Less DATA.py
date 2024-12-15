import telebot
from telebot import types
import sqlite3
bot = telebot.TeleBot('6810749735:AAHNXFI4x1tBk_IQa7UJJrjCO8swfD1zl7A')
name = None
@bot.message_handler(commands=['start'])
def start(message):
    # 1. СОЗДАНИЕ БАЗЫ ДАННЫХ
    con = sqlite3.connect('../Telegram/data.sql')
    # 2. СОЗДАНИЕ КУРСОРА ДЛЯ РАБОТЫ С БАЗОЙ
    cur = con.cursor()
    # 3. СОЗДАНИЕ ТАБЛИЦЫ
    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), password varchar(50))')
    con.commit()
    cur.close()
    con.close()
    bot.send_message(message.chat.id, 'Привет! Сейчас Вас зарегистрируем. Введите ваше имя ')
    # 4. Вызывает функцию для получения данных и регистрирует данные в таблицу
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name                   # Подключение глобальной переменной в функцию
    name = message.text.strip()   # .strip - удаляет пробелы до и после текста

    bot.send_message(message.chat.id, 'Создайте пароль: ')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    # 5. РЕГИСТРАЦИЯ В БАЗЕ ДАННЫХ. ПОВТОРЯЕМ КОД ДЛЯ СОЗДАНИЯ БАЗЫ.

    con = sqlite3.connect('../Telegram/data.sql')
    cur = con.cursor()
    # cur.execute("INSERT INTO users (name, password) VALUES ('%s', '%s')" % (name, password))
    cur.execute(f'INSERT INTO users (name, password) VALUES ("{name}", "{password}")')
    con.commit()
    cur.close()
    con.close()

    markup = types.InlineKeyboardMarkup()
    b_1 = types.InlineKeyboardButton('INFO', callback_data='users')
    markup.add(b_1)

    bot.send_message(message.chat.id, 'Пользователь успешно зарегистрирован!', reply_markup=markup)

# 6. СОЗДАЁМ ДЕКОРАТОР КОТОРЫЙ БУДЕТ ОБРАБАТЫВАТЬ callback_data=
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    con = sqlite3.connect('../Telegram/data.sql')
    cur = con.cursor()
    cur.execute("SELECT * FROM users")       # ВЫБРАТЬ ВСЕ ДАННЫЕ * ИЗ БД users
    users = cur.fetchall()                   #  ЭТА ФУНКЦИЯ ВЕРНЁТ ВСЕ НАЙДЕННЫЕ ВЫБРАННЫЕ ДАННЫЕ ИЗ БД
    info = ''
    for el in users:
        info += f'ID: {el[0]}, Имя: {el[1]}, пароль: {el[2]}\n'

    cur.close()
    con.close()

    bot.send_message(call.message.chat.id, info)



bot.polling(none_stop=True)