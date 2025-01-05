import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('6810749735:AAHNXFI4x1tBk_IQa7UJJrjCO8swfD1zl7A')
amount = 0
cur = CurrencyConverter()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello\nEnter number: \n')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'You must enter the correct values!')
        bot.register_next_step_handler(message, summa)
        return
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        b1 = types.InlineKeyboardButton('RUB/USD', callback_data='RUB/USD')
        b2 = types.InlineKeyboardButton('RUB/EUR', callback_data='RUB/EUR')
        b3 = types.InlineKeyboardButton('USD/EUR', callback_data='USD/EUR')
        b4 = types.InlineKeyboardButton('Your choice', callback_data='else')
        markup.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, 'Выберите нужные валюты.', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'You must enter the correct values!')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def converter(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        result = cur.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id,
                         f'Result {values[0]}/{values[1]} : {round(result, 2)}\n Enter new values: ')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Enter the desired currencies using the symbol "/": ')
        bot.register_next_step_handler(call.message, choice)


def choice(message):
    try:
        values = message.text.upper().split('/')
        result = cur.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Result {values[0]}/{values[1]} : {round(result, 2)}\n Enter new values: ')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Error, repeat the action again! ')
        bot.register_next_step_handler(message, choice)


bot.polling(none_stop=True)

# import telebot
# import requests
# import sqlite3
# bot = telebot.TeleBot('6810749735:AAHNXFI4x1tBk_IQa7UJJrjCO8swfD1zl7A')
# API = 'e93d99bb6863b1a797d261f54cccb745'
# name = ''
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, как вас зовут?')
#     conn = sqlite3.connect('data.sql')
#     curs = conn.cursor()
#     curs.execute("CREATE TABLE IF NOT EXISTS users(id integer primary key autoincrement, name varchar(50), age varchar(50))")
#     conn.commit()
#     curs.close()
#     conn.close()
#     bot.register_next_step_handler(message, reg_name)
# def reg_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Сколько вам лет?')
#     bot.register_next_step_handler(message, reg_age)
# def reg_age(message):
#     age = message.text.strip()
#     conn = sqlite3.connect('data.sql')
#     curs = conn.cursor()
#     curs.execute("INSERT INTO users (name, age) VALUES ('%s', '%s')" % (name, age))
#     conn.commit()
#     curs.close()
#     conn.close()
#     bot.send_message(message.chat.id, 'Регистрация прошла успешно!')
#     conn = sqlite3.connect('data.sql')
#     curs = conn.cursor()
#     curs.execute("SELECT * FROM users")
#     us = curs.fetchall()
#     info = us[-1][1]
#     curs.close()
#     conn.close()
#     bot.send_message(message.chat.id, f'В каком городе вы {info} хотели бы узнать погоду?')
# def weather(message):
#     pass
#
#
#
#
#
#
# bot.polling(none_stop=True)


# import telebot
# from telebot import types
# import sqlite3
# name = ''
# bot = telebot.TeleBot('6810749735:AAHNXFI4x1tBk_IQa7UJJrjCO8swfD1zl7A')
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     img = open('temp/image/pasta-gato-fideos-pizza-dibujo.png', 'rb')
#     bot.send_photo(message.chat.id, img)
#     bot.send_message(message.chat.id, 'Привет Кристиночка, меня зовут Куки.')
#
#     conn = sqlite3.connect('data.sql')
#     cur = conn.cursor()
#     cur.execute('CREATE TABLE IF NOT EXISTS new_users (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), age int(30))')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, "Как тебя зовут?")
#     bot.register_next_step_handler(message, reg_name)
#
#
#
#
#
#
#
# def reg_name(message):
#     global name
#     name = message.text.strip()
#
#     bot.send_message(message.chat.id, 'Введите ваш возраст: ')
#     bot.register_next_step_handler(message, reg_age)
#
# def reg_age(message):
#     age = message.text.strip()
#
#     conn = sqlite3.connect('data.sql')
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO new_users (name, age) VALUES ('%s','%s')" % (name, age))
#     conn.commit()
#     cursor.close()
#     conn.close()
#
#
#     markup = types.InlineKeyboardMarkup()
#     but_1 = types.InlineKeyboardButton('INFO', callback_data='info')
#     markup.add(but_1)
#     bot.send_message(message.chat.id, 'Пользователь успешно зарегистрирован!', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     conn = sqlite3.connect('data.sql')
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM new_users")
#     info = ''
#     user = cursor.fetchall()
#     for el in user:
#         info += f'ID: {el[0]} Имя: {el[1]} Возраст: {el[2]}\n'
#     cursor.close()
#     conn.close()
#     bot.send_message(call.message.chat.id, info)
#
#
# bot.polling(none_stop=True)
#


# import telebot
# from telebot import types
# import sqlite3
#
# bot = telebot.TeleBot('6810749735:AAHNXFI4x1tBk_IQa7UJJrjCO8swfD1zl7A')
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     img = open('C:/Users/Admin/Desktop/Programming/Telegram/temp/image/catpuaro.jpeg', 'rb')
#     bot.send_message(message.chat.id, 'Hello')
#     bot.send_photo(message.chat.id, img)
#     markup = types.InlineKeyboardMarkup()
#     but_1 = types.InlineKeyboardButton('Users', callback_data='users')
#     but_2 = types.InlineKeyboardButton('Musik', url='https://muzofond.fm/personal-music/playlists/458874')
#     markup.add(but_1, but_2)
#     bot.send_message(message.chat.id, 'Lalala', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     conn = sqlite3.connect('data.sql')
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM users')
#     users = cur.fetchall()
#     info = ''
#     for el in users:
#         info += f'ID: {el[0]}, Name: {el[1]}, Pass: {el[2]}\n'
#     cur.close()
#     conn.close()
#     bot.send_message(call.message.chat.id, info)
#
#
# bot.polling(none_stop=True)
