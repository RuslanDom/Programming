from aiogram import Dispatcher, Bot, F
from Telegram.Aiogram.bot_project.config import BOT_TOKEN, admin_id
from aiogram.filters import CommandStart, Command
from aiogram.types import ContentType
from Telegram.Aiogram.bot_project.handlers.basic import run


async def start(bot: Bot):
    await bot.send_message(admin_id, text='START BOT')


async def stop(bot: Bot):
    await bot.send_message(admin_id, text='STOP BOT')


async def bot_job():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.startup.register(start)
    dp.message.register(run, Command(commands='start'))

    dp.shutdown.register(stop)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
