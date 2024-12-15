from telebot.types import Message
from Telegram_bot.Bot_CatPush.loader import bot


@bot.message_handler(state=None)
def bot_echo(message: Message):
    bot.reply_to(message, message.text)
