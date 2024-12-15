from aiogram.utils.keyboard import InlineKeyboardBuilder


def make_inline_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Your name", callback_data="Ruslan")
    keyboard.button(text="Your lastname", callback_data="Dom")
    keyboard.button(text="Google", url='https://www.google.com')
    keyboard.adjust(2, 1)
    return keyboard.as_markup(resize_keyboard=True, selective=True, one_time_keyboard=True)









