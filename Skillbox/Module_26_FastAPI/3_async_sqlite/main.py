from typing import List

import uvicorn
from fastapi import FastAPI
from sqlalchemy.future import select

import models, schemas
from databases import engine, session
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # При запуске
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    print("Приложение запущено")
    yield
    # При остановке
    await session.close()
    await engine.dispose()


app = FastAPI(lifespan=lifespan)



@app.post("/books", response_model=schemas.BookOut)
async def books(book: schemas.BookIn) -> models.Book:
    new_book = models.Book(**book.dict())
    async with session.begin():
        session.add(new_book)
    return new_book


@app.get("/books", response_model=List[schemas.BookOut])
async def books() -> List[models.Book]:
    async with session.begin():
        books = await session.execute(select(models.Book))
        return books.scalars().all()

if __name__ == "__main__":
    uvicorn.run(app)