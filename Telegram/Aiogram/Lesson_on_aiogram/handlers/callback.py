from aiogram import Bot
from aiogram.types import CallbackQuery


async def name_lastname(call: CallbackQuery, bot: Bot):
    await call.message.answer(f'Привет {call.data}')
    await call.answer()

