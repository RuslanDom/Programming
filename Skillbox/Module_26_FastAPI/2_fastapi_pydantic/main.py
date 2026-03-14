from fastapi import FastAPI, Body
from typing import Optional
from pydantic import BaseModel, Field


# ЗАПУСК: uvicorn src:app --reload
app = FastAPI()

class Author(BaseModel):
    name: str
    born_year: int = Field(ge=0, le=2010)

class Book(BaseModel):
    title: Optional[str] = None
    author: Author
    year: Optional[int]




@app.post("/books")
@app.post("/books/{book_id}")
async def create_book(
        book: Book,
        book_id: Optional[int] = None,
        publisher: Optional[str] = Body(...)
):
    publisher_message = f"It was published by {publisher}" if publisher else ""
    return {'message': f"{book.title} {book.year} by {book.author.name}. {publisher_message}"}