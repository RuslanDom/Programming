from telebot.custom_filters import StateFilter
from loader import bot
from utils.commands import set_commands
import handlers
from models.users import create_models


if __name__ == '__main__':
    create_models()
    bot.add_custom_filter(StateFilter(bot))
    set_commands(bot)
    bot.polling()


