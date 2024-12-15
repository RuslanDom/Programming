from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot


async def set_command(bot: Bot) -> None:
    """
    Функция получения команд через кнопку meny
    """
    commands = [
        BotCommand(
            command='start',
            description='Начало работы бота'
        ),
        BotCommand(
            command='help',
            description='Справка - помощь'
        ),
        BotCommand(
            command='search',
            description='Поиск по фильтрам'
        ),
        BotCommand(
            command='result_search_by_filters',
            description='Получить найденные по фильтрам фильмы'
        ),
        BotCommand(
            command='history',
            description='Получить историю запросов пользователя'
        ),
        BotCommand(
            command='find',
            description='Поиск фильма по названию'
        ),
        BotCommand(
            command='result_search_by_word',
            description='Получить найденные по названию фильмы'
        ),
        BotCommand(
            command='clear_data',
            description='Очистить БД'
        ),
        BotCommand(
            command='clear_history',
            description='Очистить историю'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())











