from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite+aiosqlite:///./app.db"

engine = create_async_engine(DATABASE_URL, echo=True)  # echo - логгировать все sql запросы

# async_session = sessionmaker(
#     engine,
#     expire_on_commit=False,
#     class_=AsyncSession)

async_session = async_sessionmaker(engine, expire_on_commit=False)

session = async_session()

Base = declarative_base()






