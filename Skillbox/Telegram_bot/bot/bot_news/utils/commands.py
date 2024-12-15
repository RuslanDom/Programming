from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='all_news',
            description='Все новости'
        ),
        BotCommand(
            command='fresh',
            description='Последние новости'
        )
    ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())

