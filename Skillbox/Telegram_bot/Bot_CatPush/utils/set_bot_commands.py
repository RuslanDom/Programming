from telebot.types import BotCommand
from Telegram_bot.Bot_CatPush.config_data.config import DEFAULTS_COMMANDS


def set_default_commands(bot):
    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULTS_COMMANDS]
    )

