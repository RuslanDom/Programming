from aiogram.utils.keyboard import InlineKeyboardBuilder


def Year_Genres_Countries_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="По году", callback_data="category_year")
    keyboard.button(text="По жанру", callback_data="category_genres")
    keyboard.button(text="По стране производства", callback_data="category_countries")
    keyboard.button(text="ПОИСК", callback_data="no")
    keyboard.adjust(2, 2)
    return keyboard.as_markup(
        resize_keyboard=True, selective=True, one_time_keyboard=True
    )


def movie_or_series_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Фильм", callback_data="select_movie")
    keyboard.button(text="Сериал", callback_data="select_tv-series")
    return keyboard.as_markup(
        resize_keyboard=True, selective=True, one_time_keyboard=True
    )


def yes_no_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Да", callback_data="yes")
    keyboard.button(text="Нет", callback_data="no")
    return keyboard.as_markup(
        resize_keyboard=True, selective=True, one_time_keyboard=True
    )
