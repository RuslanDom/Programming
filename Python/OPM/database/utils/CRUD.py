from typing import Any, List, Dict
from peewee import ModelSelect
from OPM.database.common.models import db, BaseModel


def store_data(db: db, model, *data: List[Dict]) -> None:
    with db.atomic():
        model.insert_many(*data).execute()


def retrieve_all_data(db: db, model, *columns: BaseModel) -> ModelSelect:
    with db.atomic():
        response = model.select(*columns)
    return response


class CRUDInterface:
    @staticmethod
    def create():
        return store_data

    @staticmethod
    def retrieve():
        return retrieve_all_data


if __name__ == '__main__':
    store_data()
    retrieve_all_data()
    CRUDInterface()



