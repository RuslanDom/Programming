import os
import sqlite3
from flask import Flask, render_template, request, g

# Конфигурация
DATABASE = "/tmp/flatsite.db"
DEBUG = True
SECRET_KEY = os.urandom(10).hex()


app = Flask(__name__)
# Загружаем конфигурацию в параметре из какого модуля грузим конфиг файл, например __name__
app.config.from_object(__name__)

# Переопределение пути к БД
# app.root_path ссылается на текущий каталог запущенного приложения
app.config.update(
    dict(DATABASE=os.path.join(app.root_path, "flatsite.db"))
)


dir_path = os.path.dirname(os.path.abspath(__file__))


def connect_db():
    conn = sqlite3.connect(app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


# Функция для создания таблиц
def create_db():
    db = connect_db()
    with app.open_resource(os.path.join(dir_path, "sq_db.sql"), 'r') as f:
        cur = db.cursor()
        cur.executescript(f.read())
    db.commit()
    db.close()


@app.route("/")
def index():
    db = get_db()
    return render_template("index.html", menu=[])


def get_db():
    # Соединение с БД, если ещё не установлено
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    # Закрываем соединение с БД, если оно было не установленно
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)


# Вызывается единожды для создания БД
# create_db()
