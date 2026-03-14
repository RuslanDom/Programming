from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import os


# class Settings(BaseSettings):
#     DB_HOST: str = Field()
#     DB_PORT: int = Field()
#     DB_USER: str = Field()
#     DB_PASS: str = Field()
#     DB_NAME: str = Field()

#     @property
#     def DATABASE_URL_asyncpg(self):
#         # DSN
#         # postgresql+asyncpg://posgres:posgres@localhost:5432/ra    
#         return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

#     @property
#     def DATABASE_URL_psycopg(self):
#         # DSN
#         # postgresql+psycopg://postgres:posgres@localhost:5432/ra
#         return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

#     model_config = SettingsConfigDict(env_file=".env")

# settings = Settings()

from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_NAME = os.getenv('DB_NAME')
DB_PASS = os.getenv('DB_PASS')
URL_psycopg = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
URL_asyncpg = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"




