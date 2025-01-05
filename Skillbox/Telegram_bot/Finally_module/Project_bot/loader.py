from aiogram import Dispatcher, Bot
from Skillbox.Telegram_bot.Finally_module.Project_bot.config_data.config import BOT_TOKEN
from Skillbox.Telegram_bot.Finally_module.Project_bot.handlers import basic_handlers, get_response, set_history, echo, search_handler, help
from Skillbox.Telegram_bot.Finally_module.Project_bot.models.models import create_models
from Skillbox.Telegram_bot.Finally_module.Project_bot.utils.set_commands import set_command


async def run():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(
        basic_handlers.router,
        help.router,
        get_response.router,
        set_history.router,
        search_handler.router,
        echo.router

    )
    await set_command(bot)
    try:
        create_models()

        await dp.start_polling(bot)
    finally:
        await bot.session.close()
