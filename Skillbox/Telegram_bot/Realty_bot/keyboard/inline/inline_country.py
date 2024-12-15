from aiogram.utils.keyboard import InlineKeyboardBuilder


def set_country():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='USA', callback_data='country_united-states''')
    keyboard.button(text='Russia', callback_data='country_russia')
    keyboard.button(text='Spain', callback_data='country_spain')
    keyboard.button(text='Belarus', callback_data='country_belarus')
    keyboard.button(text='France', callback_data='country_france')
    keyboard.button(text='Greece', callback_data='country_greece')
    keyboard.button(text='Germany', callback_data='country_germany')
    keyboard.button(text='Italy', callback_data='country_italy')
    keyboard.button(text='Bulgaria', callback_data='country_bulgaria')
    keyboard.adjust(3, 3, 3)
    return keyboard.as_markup(resize_keyboard=True, selective=True, one_time_keyboard=True)


def get_inline_country():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='USA', callback_data='get_country_united-states''')
    keyboard.button(text='Russia', callback_data='get_country_russia')
    keyboard.button(text='Spain', callback_data='get_country_spain')
    keyboard.button(text='Belarus', callback_data='get_country_belarus')
    keyboard.button(text='France', callback_data='get_country_france')
    keyboard.button(text='Greece', callback_data='get_country_greece')
    keyboard.button(text='Germany', callback_data='get_country_germany')
    keyboard.button(text='Italy', callback_data='get_country_italy')
    keyboard.button(text='Bulgaria', callback_data='get_country_bulgaria')
    keyboard.adjust(3, 3, 3)
    return keyboard.as_markup(resize_keyboard=True, selective=True, one_time_keyboard=True)


