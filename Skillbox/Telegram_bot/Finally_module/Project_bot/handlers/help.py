from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from Finally_module.Project_bot.database.commands_data import history_insert

router = Router()


@router.message(Command(commands='help'))
async def get_help(message: Message) -> None:
    """
    Функция справка
    :param message: str
    :return: None
    """
    history_insert(message.from_user.id, message.text)
    text = [
        "Список команд:"
        "/start - Начало работы бота",
        "/help - Справка - помощь",
        "/search - Поиск по фильтрам",
        "/result_search_by_filters - Получить найденные по фильтрам фильмы",
        "/find - Поиск фильма по названию",
        "/result_search_by_word - Получить найденные по названию фильмы",
        "/clear_data - Очистить БД",
        "/history - Получить историю запросов пользователя",
        "/clear_history - Очистить историю"
    ]
    await message.answer('\n'.join(text))
