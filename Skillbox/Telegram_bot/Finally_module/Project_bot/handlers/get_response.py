import json
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from Finally_module.Project_bot.database.commands_data import get_data, history_insert
from Finally_module.Project_bot.utils.patter_string import set_string

router = Router()


@router.message(Command(commands="result_search_by_filters"))
async def get_result_search_by_filters(message: Message) -> None:
    """
    Функция достаёт из базы данных найденные фильмы и выводит их в формате message.answer пользователю
    :param message: str
    :return: None
    """

    history_insert(message.from_user.id, message.text)
    await message.answer("Загружаю данные по поиску...")

    result = get_data(message.from_user.id)
    if result:
        for k, v in result.items():
            await message.answer(set_string(v=v))

    else:
        await message.answer('Вы указали неверные данные!\nПроверьте ещё раз:\n'
                             'Год в формате числа (Пример: 2024)\n'
                             'Жанр в формате текста на русском яз. (Пример: комедия)\n'
                             'Страна производства в формате текста на русском яз. (Пример: США)')

