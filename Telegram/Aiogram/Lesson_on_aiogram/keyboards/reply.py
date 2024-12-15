from aiogram.utils.keyboard import ReplyKeyboardBuilder


def send_location():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='location', request_location=True)
    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=True, selective=True)



