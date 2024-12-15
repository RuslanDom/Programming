from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from bot.bot_news.utils.commands import set_commands

router = Router()


@router.message(Command(commands='start'))
async def start_message(message: Message, bot: Bot):
    await set_commands(bot)
    await message.answer('Привет {user}, добро пожаловать нв новостной канал, здесь самые свежие новости по IT\n'
                         'Если хотите получить свежие новости введите команду /fresh'
                         .format(user=message.from_user.username))



