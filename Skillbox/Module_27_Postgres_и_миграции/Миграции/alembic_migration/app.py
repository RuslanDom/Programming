import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

from fastapi import FastAPI


"""
pip install alembic
alembic init alembic - Иницализация alembic (дефолтная версия)
alembic revision --message="Init migration" --autogenerate - создание миграции, аналог commit
alembic upgrade head  - переключится на версию миграции, аналогично git pull
alembic downgrade ca00f63b78da-1  ОТКАТИТЬ ВЕРСИЮ НА ПРЕДЫДУЩУЮ
"""

app = FastAPI()
Base = declarative_base()
engine = create_async_engine('postgresql+asyncpg://postgres:postgres@localhost')
async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    email = Column(String(50))
    login = Column(String(50), nullable=False)

    # branches
    # col_from_dev1 = Column(String(50), nullable=False)
    # col_from_dev2 = Column(String(50), nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.email}, {self.login}"

async def start():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(start())

