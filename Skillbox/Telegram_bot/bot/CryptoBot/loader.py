from telebot import TeleBot
from config_data.config import BOT_TOKEN
from telebot.storage import StateMemoryStorage

storage = StateMemoryStorage()
bot = TeleBot(BOT_TOKEN, state_storage=storage)








