from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def sign_in():
    keyboard = InlineKeyboardMarkup(row_width=1)
    but1 = InlineKeyboardButton(text='Войти в систему', callback_data='sign')
    keyboard.add(but1)
    return keyboard


def registration():
    keyboard = InlineKeyboardMarkup(row_width=1)
    but1 = InlineKeyboardButton(text='Регистрация', callback_data='reg')
    keyboard.add(but1,)
    return keyboard






