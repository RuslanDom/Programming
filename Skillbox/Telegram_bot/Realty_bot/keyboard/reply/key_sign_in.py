from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from loguru import logger


@logger.catch
def sign_in() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text='Войти')
    keyboard.add(button)
    return keyboard



