"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""
import os
import shlex, subprocess
from typing import List
from flask import Flask, request

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    args: List[str] = request.args.getlist("arg")
    # Вариант 1
    result = list()
    safe_command = f"ps {shlex.quote(''.join(args))}"
    resout = os.popen(safe_command)
    for i_str in resout.readlines():
        result.append(i_str)
    return "<br>".join(result)

    # Вариант 2
    # safe_command = shlex.quote(''.join(args))
    # result = str(subprocess.check_output(["ps", safe_command]))
    # return "<br>".join(result.split(r'\n'))


if __name__ == "__main__":
    app.run(debug=True)
