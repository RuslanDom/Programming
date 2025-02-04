import os
import sqlite3
from flask import Flask, render_template, request, g


# Конфигурация
DATABASE = "/tmp/flatsite.db"
DEBUG = True
SECRET_KEY = os.urandom(10).hex()


app = Flask(__name__)
# Загружаем конфигурацию в параметре и из какого модуля грузим конфиг файл, например __name__
app.config.from_object(__name__)

# Переопределение пути к БД
# app.root_path ссылается на текущий каталог запущенного приложения
app.config.update(
    dict(DATABASE=os.path.join(app.root_path, "flatsite.db"))
)


dir_path = os.path.dirname(os.path.abspath(__file__))


def connect_db():
    conn = sqlite3.connect(app.config["DATABASE"])
    conn.row_factory = sqlite3.Row  # Данные из БД будут ввиде словаря, а не ввиде кортежа
    return conn


# Функция для создания таблиц
def create_table():
    db = connect_db()
    # Читает файл со скриптами для создания таблицы
    path = os.path.join(dir_path, "sq_db.sql")
    print(path)
    with app.open_resource(path, 'r') as f:
        cursor = db.cursor()
        # cursor.executescript(f.read())  # Выполнить прочитанный скрипт
    db.commit()
    db.close()


def get_db():
    # Соединение с БД, если ещё не установлено
    if not hasattr(g, "link_db"):  # Существует ли у БД такое св-во link_db, если нет то сделать connect_db
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    return render_template("index.html")


@app.teardown_appcontext
def close_db(error):
    # Закрываем соединение с БД, если оно было не установленно
    if hasattr(g, 'link_db'):
        g.link_db.close()


# if __name__ == "__main__":
#     app.config["WTF_CSRF_ENABLED"] = False
#     app.run(debug=True)


# Вызывается единожды для создания БД
create_table()
