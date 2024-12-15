import json
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from Project_bot.handlers.basic_handlers import last_query

router = Router()


@router.message(Command(commands="get_all"))
async def all_data(message: Message) -> None:
    """
    Функция достаёт из базы данных найденные фильмы и выводит их в формате message.answer пользователю
    :param message: str
    :return: None
    """
    last_query.append({"id": message.from_user.id, "text": message.text})
    await message.answer("Загружаю данные по поиску...")
    with open(r"database\films.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    if len(data) > 5:
        for k, v in data.items():
            response = (
                f"Название: {v['name']} (альтернативное: {v['alternativeName']})\n"
                f"Год производства: {str(v['year'])}\nРейтинг:\n\tKP: {v['rating']['kp']}\n\t"
                f"IMDB: {v['rating']['imdb']}\n\tFilmsCritics: {v['rating']['filmCritics']}\n"
                f"Страна производства: {v['countries']}\nЖанр: {v['genres']}\n"
                f"{v['poster']}"
            )
            await message.answer(response)
    else:
        await message.answer('Вы указали неверные данные!\nПроверьте ещё раз:\n'
                             'Год в формате числа (Пример: 2024)\n'
                             'Жанр в формате текста на русском яз. (Пример: комедия)\n'
                             'Страна производства в формате текста на русском яз. (Пример: США)')