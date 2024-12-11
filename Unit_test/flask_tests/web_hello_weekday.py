from flask import Flask
from datetime import datetime


DAYS = [
    "Понедельника",
    "Вторника",
    "Среды",
    "Четверга",
    "Пятницы",
    "Субботы",
    "Воскресенья"
]


app = Flask(__name__)


@app.route("/hello/<name>")
def hello_name(name):
    this_day = datetime.today().weekday()
    return f"Привет {name}, хорошего(ей) тебе {DAYS[this_day]}"









if __name__ == "__main__":
    app.run(debug=True)



