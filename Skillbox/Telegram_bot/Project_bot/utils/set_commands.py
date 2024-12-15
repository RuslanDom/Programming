from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot


async def set_command(bot: Bot) -> None:
    commands = [
        BotCommand(
            command='start',
            description='Начало работы бота'
        ),
        BotCommand(
            command='search',
            description='Поиск'
        ),
        BotCommand(
            command='get_all',
            description='Получить найденные фильмы'
        ),
        BotCommand(
            command='history',
            description='Получить историю запросов пользователя'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())











