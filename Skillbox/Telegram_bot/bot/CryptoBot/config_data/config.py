import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
API_KEY = os.getenv('API_KEY')

DB_PATH = os.path.join(r"database\users_database.db")

