from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text, String
from config import *
import asyncio
from typing import Annotated


# Создание подключения к БД (синхр)
sync_engine = create_engine(
    # url=settings.DATABASE_URL_psycopg,
    url= URL_psycopg,
    echo=True,  # Логгирование работы ОРМ
    pool_size=5,  # Сколько создать подключений к БД
    max_overflow=5   # Вызвать дополнительные подключения
)
# begin() и connect() различаются тем что begin самостоятельно в конце работы with as делает commit()
# with sync.engine.begin() as conn:
# with sync.engine.connect() as conn:
    # result = conn.execute(text("SELECT VERSION()"))  # Alchemy не работает со строками, нужно заворачивать text()
    # print(f"{result.all()=}")
    # print(f"{result.one()=}")
    # print(f"{result.first()=}")


# Асинхронная версия 
my_async_engine = create_async_engine(
    url= URL_asyncpg,
    echo=True
)
# async def task_1():
#     async with my_async_engine.connect() as conn:
#         res = await conn.execute(text("SELECT 1, 2, 3 union SELECT 4, 5, 6"))
#     print(f"{res.all()=}")
# asyncio.run(task_1())

# sessionmaker для того чтобы не прописывать каждый раз with Session() as session
sync_session = sessionmaker(sync_engine)
async_session = async_sessionmaker(my_async_engine)


str_256 = Annotated[str, 200]

class Base(DeclarativeBase):
    type_annotaion_map = {
        str_256: String(256)
    }








