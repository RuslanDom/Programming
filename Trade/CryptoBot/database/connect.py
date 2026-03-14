import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv



class DataBase:
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")
    Base = declarative_base()
    engine = create_async_engine(DATABASE_URL, echo=True)

    def __init__(self):
        self.AsyncSession = async_sessionmaker(self.engine, expire_on_commit=False)
        self.session = self.AsyncSession()

        # Синхронная сессия
        # self.Session = sessionmaker(bind=self.engine, expire_on_commit=False)
        # self.sync_session = self.Session()

    @classmethod
    async def create_db(cls):
        async with cls.engine.begin() as conn:
            await conn.run_sync(cls.Base.metadata.create_all)


