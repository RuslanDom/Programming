from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from Project_bot.state.User_state import UserState
from peewee import IntegrityError
from Project_bot.models.models import UserHistory
from Project_bot.keyboards.inline import (
    movie_or_series_keyboard,
    Year_Genres_Countries_keyboard,
    yes_no_keyboard,
)
from Project_bot.utils.parser_films import parser
from loguru import logger
from Project_bot.utils.set_commands import set_command

router = Router()
last_query = []


@router.message(Command(commands="start"))
async def start(message: Message, state: FSMContext, bot: Bot):
    await set_command(bot)
    last_query.append({"id": message.from_user.id, "text": message.text})
    await state.set_state(UserState.user_id)
    await message.answer(f"Добро пожаловать {message.from_user.username}!")
    await state.update_data(user_id=message.from_user.id)
    context_data = await state.get_data()
    user = message.from_user.id
    try:
        UserHistory.create(user_id=user, user_history=["start"])
    except IntegrityError:
        pass


@router.message(Command(commands="search"))
async def search_films(message: Message, state: FSMContext):
    last_query.append({"id": message.from_user.id, "text": message.text})
    await state.update_data(year='2024', genres="комедия", countries="США")
    parameters = await state.get_data()
    logger.info(parameters["year"], parameters["genres"], parameters["countries"])
    await message.answer(
        "Выберите что вас интересует (фильм или сериал)",
        reply_markup=movie_or_series_keyboard(),
    )
    await state.set_state(UserState.type)


@router.callback_query(F.data.startswith("select_"))
async def type_movie(call: CallbackQuery, state: FSMContext):
    last_query.append({"id": call.message.from_user.id, "text": call.data})
    await state.update_data(type=call.data.replace("select_", ""))

    await call.message.edit_reply_markup()
    await call.message.answer(
        "Вы берите дополнительные параметры поиска", reply_markup=Year_Genres_Countries_keyboard()
    )


@router.callback_query(F.data.startswith("category_"))
async def category_movie(call: CallbackQuery, state: FSMContext):
    last_query.append({"id": call.message.from_user.id, "text": call.data})
    data = call.data.replace("category_", "")
    await call.message.edit_reply_markup()

    if data == "year":
        await call.message.answer("Введите год производства")
        await state.set_state(UserState.year)
    elif data == "genres":
        await call.message.answer("Введите желаемый жанр")
        await state.set_state(UserState.genres)
    elif data == "countries":
        await call.message.answer("Введите страну производства")
        await state.set_state(UserState.countries)


@router.message(UserState.year)
async def set_year(message: Message, state: FSMContext, bot: Bot):
    last_query.append({"id": message.from_user.id, "text": message.text})
    await state.update_data(year=message.text)
    await bot.send_message(
        message.from_user.id,
        "Добавить фильтры для поиска",
        reply_markup=yes_no_keyboard(),
    )


@router.message(UserState.genres)
async def set_genres(message: Message, state: FSMContext, bot: Bot):
    last_query.append({"id": message.from_user.id, "text": message.text})
    await state.update_data(genres=message.text.lower())
    await bot.send_message(
        message.from_user.id,
        "Добавить фильтры для поиска",
        reply_markup=yes_no_keyboard(),
    )


@router.message(UserState.countries)
async def set_countries(message: Message, state: FSMContext, bot: Bot):
    last_query.append({"id": message.from_user.id, "text": message.text})
    refactoring_name = lambda x: (
        x.capitalize() if x != "сша" and x != "США" and x != "Сша" else x.upper()
    )
    result = refactoring_name(message.text)
    await state.update_data(countries=result)
    await bot.send_message(
        message.from_user.id,
        "Добавить фильтры для поиска",
        reply_markup=yes_no_keyboard(),
    )


@router.callback_query(F.data == "yes")
async def yes_(call: CallbackQuery):
    last_query.append({"id": call.message.from_user.id, "text": call.data})
    await call.message.edit_reply_markup()
    await call.message.answer("OK", reply_markup=Year_Genres_Countries_keyboard())


@router.callback_query(F.data == "no")
async def no_(call: CallbackQuery, state: FSMContext):
    last_query.append({"id": call.message.from_user.id, "text": call.data})
    await call.message.edit_reply_markup()
    parameters = await state.get_data()
    await state.clear()
    parser(
        type_=parameters["type"],
        year=parameters["year"],
        genres=parameters["genres"],
        countries=parameters["countries"],
    )
    await call.message.answer(
        "Если вы хотите получить все данные используйте команду /get_all"
    )
