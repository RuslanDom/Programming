from loader import bot
from telebot.types import Message
from utils.log_err import log_error


@log_error
@bot.message_handler(commands=['help'])
def help_command(message: Message):
    text = ("Список всех команд:\n",
            "/start - запуск бота\n",
            "/help - справка\n",
            "/sign_in - войти в систему")
    bot.send_message(message.from_user.id, ''.join(text))
