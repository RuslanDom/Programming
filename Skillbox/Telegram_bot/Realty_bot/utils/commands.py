from telebot.types import BotCommand, BotCommandScopeDefault
from loguru import logger
from aiogram import Bot


async def set_commands(bot: Bot):
    commands = [
         BotCommand(
             command='start',
             description='Начало работы'
         ),
         BotCommand(
             command='help',
             description='Справка'
         ),
         BotCommand(
             command='set_data',
             description='Заполнить базу данных'
         ),
         BotCommand(
             command='get',
             description='Получить объявления'
         )
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())


from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot


