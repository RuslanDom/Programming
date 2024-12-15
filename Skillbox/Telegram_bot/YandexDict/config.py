import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv("API_KEY")
URL = 'https://dictionary.yandex.net/api/v1/dicservice.json'
DEFAULT_LANG = 'ru-en'
