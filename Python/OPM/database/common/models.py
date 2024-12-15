from datetime import datetime
from peewee import *

db = SqliteDatabase("lecture.db")


class BaseModel(Model):
    created_at = DateField(default=datetime.now())

    class Meta:
        database = db


class History(BaseModel):
    number = TextField()
    message = TextField()
    






