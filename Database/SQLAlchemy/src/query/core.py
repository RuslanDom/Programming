from model import metadata_obj, workers_table
from database import sync_engine
from sqlalchemy import text, insert


def create_table():
    sync_engine.echo = False  # откл логи
    metadata_obj.drop_all(sync_engine)  # Удалить все таблицы
    metadata_obj.create_all(sync_engine)  # Создать все таблицы
    sync_engine.echo = True  # вкл логи


def insert_data():
    with sync_engine.connect() as conn:
        # statement = """INSERT INTO workers(username) VALUES('Bobr'), ('Volk');"""
        # conn.execute(text(statement))

        # Используем query builder, insert(таблица в которую планируется вставка)
        statement = insert(workers_table).values(
            [
                {"username": "Bobr"},
                {"username": "Volk"}
            ]
        )
        conn.execute(statement)
        conn.commit()


