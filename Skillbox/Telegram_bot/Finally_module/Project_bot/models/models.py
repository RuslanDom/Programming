from peewee import *
from Finally_module.Project_bot.config_data.config import DB_PATH

db = SqliteDatabase("database/common_base.db")


class Basemodel(Model):
    class Meta:
        database = db


class FoundItems(Basemodel):
    user_id = IntegerField()
    result_data = TextField()

    class Meta:
        db_table = 'results'


class UserHistory(Basemodel):
    """
    user_id  - будет получать и сохранять ID пользователя
    user_history - сохраняет команды, которые будет отправлять пользователь
    """
    user_id = IntegerField()
    user_history = TextField()

    class Meta:
        db_table = "histories"


def create_models():
    with db:
        db.create_tables(Basemodel.__subclasses__())
        # db.create_tables([UserHistory]) Можно было так написать
