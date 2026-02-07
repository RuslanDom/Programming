from flask import Flask
import time
import flask_profiler
from sqlalchemy import create_engine

"""Перегрузка flask энкодера"""
import flask.json
import decimal

class NewEncoder(flask.json):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(NewEncoder, self).default(o)


app = Flask(__name__)
engine = create_engine('sqlite:///flask_profiler.db')
app.json_encoder = NewEncoder

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
    """
    app.run(debug=True)