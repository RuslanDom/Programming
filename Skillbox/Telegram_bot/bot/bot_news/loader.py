from aiogram import Bot, Dispatcher
from bot.bot_news.config import BOT_TOKEN
from bot.bot_news.handlers import start, get_news


async def run():
    bot = Bot(BOT_TOKEN, parse_mode='html')
    dp = Dispatcher()
    dp.include_routers(
        start.router,
        get_news.router
    )

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


