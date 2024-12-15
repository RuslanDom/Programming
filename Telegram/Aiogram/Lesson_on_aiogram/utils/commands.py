from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot


async def set_command(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='location',
            description='Получить местоположение'
        ),
        BotCommand(
            command='pay',
            description='Купить продукт'
        ),
        BotCommand(
            command='box',
            description='Купить перчатки для бокса'
        ),
        BotCommand(
            command='lot1',
            description='Test lot1'
        ),
        BotCommand(
            command='form',
            description='Машина состояний'
        ),
        BotCommand(
            command='photo',
            description='Получить картинку'
        ),
        BotCommand(
            command='video',
            description='Получить видео'
        ),
        BotCommand(
            command='sticker',
            description='Получить стикер'
        ),
        BotCommand(
            command='audio',
            description='Получить аудиофайл'
        ),
        BotCommand(
            command='media',
            description='Получить медиа группу'
        ),
        BotCommand(
            command='slipknot',
            description='Запустить Slipknot'
        )
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())














# from aiogram.types import BotCommand, BotCommandScopeDefault
# from aiogram import Bot
#
#
# async def set_commands(bot: Bot):
#     command = [
#         BotCommand(command='help',
#                    description='Помощь'),
#         BotCommand(command='send_image',
#                    description='Получить картинку'),
#         BotCommand(command='How?',
#                    description='Как дела?')
#                 ]
#
#     # Установить команды боту, scope - кому будут видны данные команды
#     await bot.set_my_commands(command, BotCommandScopeDefault())
