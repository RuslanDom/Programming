from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command(commands=['help']))
async def command_help(message: Message, bot: Bot):
    text = (
        'Основные команды:\n',
        '/start - Запуск бота\n',
        '/help - Справка\n',
        '/set_data - Загрузить страну\n',
        '/get - Получить объявления'
    )
    await bot.send_message(message.from_user.id, ''.join(text))







