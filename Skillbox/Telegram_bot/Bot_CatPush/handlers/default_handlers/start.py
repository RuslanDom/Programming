from telebot.types import Message
from Telegram_bot.Bot_CatPush.loader import bot


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.reply_to(message, f"Привет, {message.from_user.full_name}")
