from databases import Base
from sqlalchemy import Column, String, Integer


class Book(Base):
    __tablename__ = 'Books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)