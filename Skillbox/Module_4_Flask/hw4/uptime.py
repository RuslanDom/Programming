"""
Напишите GET-эндпоинт /uptime, который в ответ на запрос будет выводить строку вида f"Current uptime is {UPTIME}",
где UPTIME — uptime системы (показатель того, как долго текущая система не перезагружалась).

Сделать это можно с помощью команды uptime.
"""

from flask import Flask
import os

app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    command = 'uptime -p'
    UPTIME = os.popen(command)
    return f"Current uptime is {UPTIME.read()}"


if __name__ == '__main__':
    app.run(debug=True)
