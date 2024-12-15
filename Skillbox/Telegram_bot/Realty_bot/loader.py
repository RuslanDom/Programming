from aiogram import Bot, Dispatcher, Router
from Realty_bot.config_data.config import BOT_TOKEN
from Realty_bot.handlers.default_handlers import start, help, get_page, set_database

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def run():
    dp.include_routers(
        start.router,
        help.router,
        set_database.router,
        get_page.router
    )

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
