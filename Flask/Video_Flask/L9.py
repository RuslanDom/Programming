from flask import Flask, g, render_template
import sqlite3
import os
from fdatabase import FDatabase
import logging, logging.config
from utils.logger_config import dict_config


# Config
DATABASE = "tmp/flatsite.db"
SECRET_KEY = os.urandom(10).hex()
DEBUG = True


logger = logging.getLogger(__name__)
logging.config.dictConfig(dict_config)
logger.setLevel("DEBUG")
# print(logger)

app = Flask(__name__)
app.config.from_object(__name__)


app.config.update(dict(DATABASE=os.path.join(app.root_path, "flatsite.db")))
logger.debug("Include config success")


def connect_db():
    logger.debug("Start connect")
    conn = sqlite3.connect(app.config["DATABASE"])
    conn.row_factory = sqlite3.Row # Он поддерживает доступ к результату запроса как к словарю, где ключ это имя столбца.
                                # Так же поддерживает обращение к столбцу по индексу, итерацию по строкам запроса,
                                # проверку на равенство и встроенную функцию len() для подсчета количества строк запроса.
    return conn


def get_db_only_in_app():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    logger.debug("Get g")
    return g.link_db


def insert_menu():
    try:
        db = connect_db()
        path = os.path.join(app.root_path, "sql_commands/insert_menu.sql")
        print(path)
        with app.open_resource(path, 'r') as f:
            cur = db.cursor()
            cur.executescript(f.read())
        db.commit()
        db.close()
        logger.info('Success insert')
    except BaseException as e:
        logger.exception("Error insert database", e)


def create_table():
    try:
        conn = connect_db()
        cur = conn.cursor()
        path = os.path.join(app.root_path, "sql_commands/create_table_mainmenu.sql")
        print(path)
        with app.open_resource(path, 'r') as f:
            cur.executescript(f.read())
        conn.commit()
        conn.close()
        logger.info("Success create table mainmenu")
    except BaseException as e:
        logger.exception("Error create table", e)


@app.route("/")
def index():
    logger.debug("Подключение ...")
    db = get_db_only_in_app()
    dbase = FDatabase(db)  # Создаём экземпляр класса где инициализируем connect и cursor
    logger.debug("index.html загружена")
    return render_template("index.html", menu=dbase.getMenu())



@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        logger.debug("Stop session g.link_db")
        g.link_db.close()


# insert_menu()
# create_table()
if __name__ == "__main__":
    logger.debug("Start app")
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)















