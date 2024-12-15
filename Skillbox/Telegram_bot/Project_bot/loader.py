from aiogram import Dispatcher, Bot
from Project_bot.config_data.config import BOT_TOKEN
from Project_bot.handlers import basic_handlers, get_response, set_history, echo
from Project_bot.models.models import create_models


async def run():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(
        basic_handlers.router,
        get_response.router,
        set_history.router,
        echo.router
    )

    try:
        create_models()

        await dp.start_polling(bot)
    finally:
        await bot.session.close()
