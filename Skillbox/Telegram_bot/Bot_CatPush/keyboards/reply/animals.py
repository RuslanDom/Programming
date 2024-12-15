from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def cat_dog():
    keyboard = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('CAT', callback_data="cat")
    button_2 = InlineKeyboardButton('DOG', callback_data="dog")
    keyboard.add(button_1, button_2)
    return keyboard
