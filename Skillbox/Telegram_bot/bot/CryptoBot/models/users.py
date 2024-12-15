from peewee import *
from config_data.config import DB_PATH


db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    username = CharField()
    firstname = CharField()
    lastname = CharField(null=True)
    wallet = CharField()
    phone_number = IntegerField()


# Вспомогательная функция, которая создаст все наши модели в базе данных:
def create_models():
    db.create_tables(BaseModel.__subclasses__())


