import os
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
API_KEY = os.getenv("API_KEY")

# DB_NAME = "history_data.db"
# DB_PATH = os.path.join(r'..\Project_bot\database\common_base.db')
DB_PATH = 'common_base.db'
DOCUMENTATION_API = "https://kinopoisk.dev/documentation"