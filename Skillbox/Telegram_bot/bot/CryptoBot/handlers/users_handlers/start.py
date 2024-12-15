from loader import bot
from telebot.types import Message
from bot.CryptoBot.utils.log_err import log_error


@log_error
@bot.message_handler(commands=['start'])
def start_command(message: Message):
    bot.send_message(message.from_user.id, 'Добро пожаловать!')


