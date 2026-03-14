# Инициализация alembic
# \Module_27_Postgres_и_миграции\Миграции\AlembicTest> alembic init src/migrations

#


import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

from fastapi import FastAPI

engine = create_async_engine("postgresql+asyncpg://postgres:postgres@localhost/database")
async_session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
app = FastAPI()


class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, default=18)






async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(startup())
