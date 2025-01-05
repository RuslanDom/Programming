import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('6810749735:AAHNXFI4x1tBk_IQa7UJJrjCO8swfD1zl7A')
convert = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, введите сумму: ')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    amount = message.text.strip()
    markup = types.InlineKeyboardMarkup(row_width=2)
    but_1 = types.InlineKeyboardButton('USD/RUB', callback_data='usd/rub')
    but_2 = types.InlineKeyboardButton('RUB/USD', callback_data='rub/usd')
    but_3 = types.InlineKeyboardButton('EUR/RUB', callback_data='eur/rub')
    but_4 = types.InlineKeyboardButton('RUB/EUR', callback_data='rub/eur')
    but_5 = types.InlineKeyboardButton('Другое значение', callback_data='else')
    markup.add(but_1, but_2, but_3, but_4, but_5)
    bot.send_message(message.chat.id, 'Выбирите валюту', reply_markup=markup)


bot.polling(none_stop=True)