from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from Skillbox.Telegram_bot.Finally_module.Project_bot.api.search_by_filtres import get_search_by_filter
from Skillbox.Telegram_bot.Finally_module.Project_bot.database.commands_data import insert_data, clear_search_data, history_insert
from Skillbox.Telegram_bot.Finally_module.Project_bot.state.User_state import UserState

from Skillbox.Telegram_bot.Finally_module.Project_bot.keyboards.inline import (
    movie_or_series_keyboard,
    Year_Genres_Countries_keyboard,
    yes_no_keyboard,
)

from loguru import logger


router = Router()
# Список в который будут сохраняться все действия пользователя


@router.message(Command(commands="start"))
async def start(message: Message, state: FSMContext) -> None:
    history_insert(message.from_user.id, message.text)
    # Инициализация записи id в машину состояний
    await state.set_state(UserState.user_id)
    # Сообщение приветствия
    await message.answer(f"Добро пожаловать {message.from_user.username}!")
    # Запись в машину состояний id пользователя
    await state.update_data(user_id=message.from_user.id)




@router.message(Command(commands='clear_data'))
async def clear_all_searchdata(message: Message):
    history_insert(message.from_user.id, message.text)
    clear_search_data(message.from_user.id)


@router.message(Command(commands="search"))
async def search_films(message: Message, state: FSMContext) -> None:
    history_insert(message.from_user.id, message.text)
    # Запись в машину состояний дефолтных настроек фильтра поиска
    await state.update_data(year='2024', genres="комедия", countries="США")
    await state.update_data(user_id=message.from_user.id)
    # Получение данных машины состояний
    parameters = await state.get_data()
    logger.info(parameters["year"], parameters["genres"], parameters["countries"])
    # Информационное сообщение с клавиатурой
    await message.answer(
        "Выберите что вас интересует (фильм или сериал)",
        reply_markup=movie_or_series_keyboard(),
    )
    # Инициализация машины состояний, поле тип (фильм или сериал)
    await state.set_state(UserState.type)


@router.callback_query(F.data.startswith("select_"))
async def type_movie(call: CallbackQuery, state: FSMContext) -> None:
    parameters = await state.get_data()
    history_insert(parameters["user_id"], call.data)
    # Запись в машину состояний выбранного типа (фильм или сериал)
    await state.update_data(type=call.data.replace("select_", ""))
    # Удаление клавиатуры
    await call.message.edit_reply_markup()
    # Информационное сообщение по параметрам поиска с клавиатурой
    await call.message.answer(
        "Вы берите дополнительные параметры поиска", reply_markup=Year_Genres_Countries_keyboard()
    )


@router.callback_query(F.data.startswith("category_"))
async def category_movie(call: CallbackQuery, state: FSMContext) -> None:
    parameters = await state.get_data()
    history_insert(parameters["user_id"], call.data)
    data = call.data.replace("category_", "")
    # Удаление клавиатуры
    await call.message.edit_reply_markup()
    # Проверка выбранного пользователем фильтра
    if data == "year":
        await call.message.answer("Введите год производства")
        # Инициализация машины состояний, параметр - год
        await state.set_state(UserState.year)
    elif data == "genres":
        await call.message.answer("Введите желаемый жанр")
        # Инициализация машины состояний, параметр - жанр
        await state.set_state(UserState.genres)
    elif data == "countries":
        await call.message.answer("Введите страну производства")
        # Инициализация машины состояний, параметр - страна производства
        await state.set_state(UserState.countries)


@router.message(UserState.year)
async def set_year(message: Message, state: FSMContext, bot: Bot) -> None:
    history_insert(message.from_user.id, message.text)
    # Запись в машину состояний параметра - год
    await state.update_data(year=message.text)
    # Сообщение пользователю о продолжении или окончании выбора дополнительных параметров поиска
    await bot.send_message(
        message.from_user.id,
        "Добавить фильтры для поиска",
        reply_markup=yes_no_keyboard(),
    )


@router.message(UserState.genres)
async def set_genres(message: Message, state: FSMContext, bot: Bot) -> None:
    history_insert(message.from_user.id, message.text)
    # Запись в машину состояний параметра - жанр
    await state.update_data(genres=message.text.lower())
    # Сообщение пользователю о продолжении или окончании выбора дополнительных параметров поиска
    await bot.send_message(
        message.from_user.id,
        "Добавить фильтры для поиска",
        reply_markup=yes_no_keyboard(),
    )


@router.message(UserState.countries)
async def set_countries(message: Message, state: FSMContext, bot: Bot) -> None:
    history_insert(message.from_user.id, message.text)
    # Рефакторинг страны (США) для поиска
    refactoring_name = lambda x: (
        x.capitalize() if x != "сша" and x != "США" and x != "Сша" else x.upper()
    )
    result = refactoring_name(message.text)
    # Запись в машину состояний параметра - страна производства
    await state.update_data(countries=result)
    # Сообщение пользователю о продолжении или окончании выбора дополнительных параметров поиска
    await bot.send_message(
        message.from_user.id,
        "Добавить фильтры для поиска",
        reply_markup=yes_no_keyboard(),
    )


@router.callback_query(F.data == "yes")
async def yes_(call: CallbackQuery, state: FSMContext) -> None:
    """
    Callback - функция на полученный ответ продолжения выбора дополнительных фильтров поиска
    :param call: CallbackQuery
    :return: None
    """
    parameters = await state.get_data()
    history_insert(parameters["user_id"], call.data)
    await call.message.edit_reply_markup()
    await call.message.answer("OK", reply_markup=Year_Genres_Countries_keyboard())


@router.callback_query(F.data == "no")
async def no_(call: CallbackQuery, state: FSMContext) -> None:
    """
    Callback - функция окончания выбора фильтров поиска и запуска парсера по указанным параметрам фильтров поиска
    :param call: CallbackQuery
    :param state:
    :return:
    """

    # Удаление клавиатуры
    await call.message.edit_reply_markup()
    # Получение данных машины состояний и запись в переменную
    parameters = await state.get_data()
    history_insert(parameters["user_id"], call.data)
    # Запуск функции - парсинга(web scraping)

    insert_data(user_id=int(parameters["user_id"]), get_result=get_search_by_filter(
        type_=parameters["type"],
        year=parameters["year"],
        genres=parameters["genres"],
        countries=parameters["countries"],
    ))
    # Очистка машины состояний
    await state.clear()
    # Информационное сообщение
    await call.message.answer(
        "Если вы хотите получить все данные используйте команду /result_search_by_filters"
    )
