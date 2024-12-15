from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from Finally_module.Project_bot.state.User_state import UserState
from Finally_module.Project_bot.api.search_of_name import search
from Finally_module.Project_bot.database.commands_data import insert_data, get_data, history_insert


from Finally_module.Project_bot.utils.patter_string import set_string

router = Router()


@router.message(Command(commands="find"))
async def search_by_word(message: Message, state: FSMContext) -> None:
    """
    Предварительная функция для получения данных от пользователя для поиска по названию
    """
    history_insert(message.from_user.id, message.text)
    await message.answer("Напишите название или ключевое слово")
    await state.set_state(UserState.key_word)


@router.message(UserState.key_word)
async def get_word(message: Message, state: FSMContext) -> None:
    """
    Функция получающая название, запускающая алгоритм поиска и сохранения результатов в БД
    """
    history_insert(message.from_user.id, message.text)
    await state.update_data(key_word=message.text)
    user_answer = await state.get_data()
    need_word = user_answer.get("key_word")
    insert_data(user_id=int(message.from_user.id), get_result=search(query=need_word))

    await state.clear()
    await message.answer(f'Поиск закончен\nВывести результаты /result_search_by_word')


@router.message(Command(commands="result_search_by_word"))
async def get_result_search_by_word(message: Message) -> None:
    """
    Функция вывода результатов поиска
    """
    history_insert(message.from_user.id, message.text)
    result = get_data(message.from_user.id)
    if result:
        for k, v in result.items():
            await message.answer(set_string(v=v))
    else:
        await message.answer("База данных пуста")
