from loguru import logger
from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from Realty_bot.utils.commands import set_commands

router = Router()


@router.message(Command(commands='start'))
async def command_start(message: Message, bot: Bot):
    await set_commands(bot)
    await message.answer('Добро пожаловать\nОсновные команды это /set_data и /get')








