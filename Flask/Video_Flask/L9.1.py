import sqlite3
from fdatabase import FDatabase
from flask import Flask, g, render_template
import os

# config
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flatsite.db")
DEBUG = True
SECURITY = os.urandom(10).hex()

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    with sqlite3.connect(app.config["DATABASE"]) as conn:
        conn.row_factory = sqlite3.Row
        return conn


def create_table():
    db = connect_db()
    cur = db.cursor()
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sql_commands/create_table.sql")
    with app.open_resource(path, 'r') as f:
        cur.executescript(f.read())
        db.commit()



def get_db_app():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def get_index_page():
    db = get_db_app()
    dbase = FDatabase(db)
    return render_template('index.html', menu=dbase.getMenu())


@app.teardown_appcontext
def close_db_app(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)


# def insert():
#     db = connect_db()
#     dbase = FDatabase(db)
#     dbase.setMenu("Главная", "/")
#     dbase.setMenu("О нас", "/about")
#     dbase.setMenu("Контакты", "/contact")


# insert()


