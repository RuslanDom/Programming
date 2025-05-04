import operator
from flask import Flask
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)


@jsonrpc.method('calc.add')
def add(a: float, b: float) -> float:
    """
    Пример запроса:

    $ curl -i -X POST -H "Content-Type: application/json; indent=4" \
        -d '{
            "jsonrpc": "2.0",
            "method": "calc.add",
            "params": {"a": 7.8, "b": 5.3},
            "id": "1"
        }' http://localhost:5000/api

    Пример ответа:

    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.10.6
    Date: Fri, 09 Dec 2022 19:00:09 GMT
    Content-Type: application/json
    Content-Length: 54
    Connection: close

    {
      "id": "1",
      "jsonrpc": "2.0",
      "result": 13.1
    }
    """
    return operator.add(a, b)


@jsonrpc.method('calc.sub')
def sub(a: float, b: float) -> float:
    """
    Запрос:

    $ curl -i -X POST -H "Content-Type: application/json; indent=4" \
       -d '{
           "jsonrpc": "2.0",
           "method": "calc.sub",
           "params": {"a": 7.8, "b": 5.3},
           "id": "2"
       }' http://localhost:5000/api

    Ответ:

    HTTP/1.1 200 OK
    Server: Werkzeug/3.1.3 Python/3.12.3
    Date: Wed, 16 Apr 2025 12:26:49 GMT
    Content-Type: application/json
    Content-Length: 53
    Connection: close

    {
      "id": "2",
      "jsonrpc": "2.0",
      "result": 2.5
    }
   """
    return operator.sub(a, b)


@jsonrpc.method('calc.multiply')
def multiply(a: float, b: float) -> float:
    """
    Запрос:

    $ curl -i -X POST -H "Content-Type: application/json; indent=4" \
       -d '{
           "jsonrpc": "2.0",
           "method": "calc.sub",
           "params": {"a": 7.0, "b": 5.0},
           "id": "3"
       }' http://localhost:5000/api

    Ответ:

    HTTP/1.1 200 OK
    Server: Werkzeug/3.1.3 Python/3.12.3
    Date: Wed, 16 Apr 2025 12:28:07 GMT
    Content-Type: application/json
    Content-Length: 54
    Connection: close

    {
      "id": "3",
      "jsonrpc": "2.0",
      "result": 35.0
    }

    """
    return operator.mul(a, b)


@jsonrpc.method('calc.divide')
def divide(a: float, b: float) -> float:
    """
    Запрос:

    $ curl -i -X POST -H "Content-Type: application/json; indent=4" \
       -d '{
           "jsonrpc": "2.0",
           "method": "calc.sub",
           "params": {"a": 10.0, "b": 5.0},
           "id": "4"
       }' http://localhost:5000/api

    Ответ:

    HTTP/1.1 200 OK
    Server: Werkzeug/3.1.3 Python/3.12.3
    Date: Wed, 16 Apr 2025 12:32:47 GMT
    Content-Type: application/json
    Content-Length: 53
    Connection: close

    {
      "id": "4",
      "jsonrpc": "2.0",
      "result": 5.0
    }
    """
    return operator.truediv(a, b)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
