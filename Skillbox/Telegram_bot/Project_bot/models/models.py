from peewee import *
from Project_bot.config_data.config import DB_PATH

db = SqliteDatabase(DB_PATH)


class Basemodel(Model):
    class Meta:
        database = db


class UserHistory(Basemodel):
    """
    user_id  - будет получать и сохранять ID пользователя
    user_history - сохраняет команды, которые будет отправлять пользователь
    """
    user_id = PrimaryKeyField(unique=True)
    user_history = CharField()

    class Meta:
        db_table = "histories"


def create_models():
    with db:
        db.create_tables(Basemodel.__subclasses__())
        # db.create_tables([UserHistory]) Можно было так написать
