from flask import Flask
import time
import flask_profiler
from sqlalchemy import create_engine

from flask.json.provider import DefaultJSONProvider
import decimal

import datetime

"""
Библиотека flask-profiler берет из базы SQLite временную метку (timestamp). В новых версиях SQLAlchemy и Python 
это значение возвращается как Decimal, а функция datetime.utcfromtimestamp() требует строго int или float 
"""
# # Создаем класс-обертку
# class DatetimePatcher:
#     def __getattr__(self, name):
#         return getattr(datetime.datetime, name)
#
#     def utcfromtimestamp(self, t):
#         if isinstance(t, decimal.Decimal):
#             t = float(t)
#         return datetime.datetime.utcfromtimestamp(t)
#
#
# # Создаем объект-заплатку
# patched_datetime = DatetimePatcher()
#
# # Принудительно заменяем datetime в модуле профайлера, если он уже загружен или будет загружен
# import flask_profiler.storage.sql_alchemy as sa_storage
#
# sa_storage.datetime = patched_datetime

app = Flask(__name__)

# Custom JSON encoder (Кастомный энкодер данных Decimal в Integer или Float)

# class UpdatedJSONProvider(DefaultJSONProvider):
#     def default(self, obj):
#         if isinstance(obj, decimal.Decimal):
#             return int(obj) if obj % 1 == 0 else float(obj)
#         return super().default(obj)
#
#
# app.json = UpdatedJSONProvider(app)

engine = create_engine('sqlite:///flask_profiler.db')

@app.route('/one')
def one():
    return "one"

@app.route('/two')
def two():
    time.sleep(3)
    return "two"

@app.route('/three')
def three():
    l = []
    for i in range(1000000):
        l.append(i)
    return "three"

@app.route('/four')
def four():
    return "four"


app.config["flask_profiler"] = {
    "enabled": True,
    "storage": {
        "engine": "sqlalchemy",
        "db_url": "sqlite:///flask_profiler.db"
    },
    "basicAuth": {
        "enabled": True,
        "username": "admin",
        "password": "admin"
    }
}

flask_profiler.init_app(app)


if __name__ == '__main__':
    """
    localhost/flask-profiler для просмотра профилирования
    
    Исправление устаревшего flask-profiler
    1. Откройте файл: C:\Users\Admin\NewProjects\.venv\Lib\site-packages\flask_profiler\storage\sql_alchemy.py
    2. Найдите строку замените её на: 
        # Было:
        rows = [datetime.utcfromtimestamp(row[0]).strftime(dateFormat) for row in rows]
        # Стало:
        rows = [datetime.utcfromtimestamp(float(row[0])).strftime(dateFormat) for row in rows]
    """
    app.run(debug=True)