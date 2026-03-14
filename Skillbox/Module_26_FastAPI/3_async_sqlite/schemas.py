from pydantic import BaseModel


class BaseBook(BaseModel):
    title: str
    author: str

class BookIn(BaseBook):
    ...

class BookOut(BaseModel):
    id: int

    class Config:
        orm_mode = True