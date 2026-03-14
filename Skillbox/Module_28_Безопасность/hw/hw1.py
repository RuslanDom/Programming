"""
Потренируемся работать с CORS. Из материалов модуля мы знаем, что есть четыре хедера,
которые помогают управлять политикой CORS. Давайте ими воспользуемся. Вам нужно дописать пример из модуля
таким образом, чтобы по CORS-политике проходили только методы POST и GET. Не забудьте добавить
эндпоинты для обработки этих методов, а также разрешить использование хедера X-My-Fancy-Header.
В качестве разрешенного источника выберите сайт по своему усмотрению. Не забудьте сделать это
с помощью декоратора, который мы разобрали ранее.
"""
from flask import Flask, jsonify, request, Response

# Через console DevTools запускаем JS script
"""
fetch(
    'http://127.0.0.1:5000',
    {method: 'GET'}
)
.then(resp=>resp.text())
.then(console.log)
"""
app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST', 'DELETE', 'PUT'])
def users_handler():
    if request.method == 'GET':
        return jsonify({"request": "GET"}), 200
    elif request.method == 'POST':
        data = request.get_json() or request.form.to_dict()
        print(data)
        return jsonify({"request": "POST"}), 201
    elif request.method == 'DELETE':
        print("DELETE")
        return jsonify({"request": "DELETE"}), 204
    elif request.method == 'PUT':
        print("PUT")
        return jsonify({"request": "PUT"}), 201


# Другой способ разрешить для всех endpoint отправлять запросы с другого источника
@app.after_request
def add_cors_headers(response: Response) -> Response:
    response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('Access-Control-Allow-Origin', 'https://www.google.com')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST')
    # Разрешаем основные заголовки
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Expose-Headers', 'X-Another-Custom-Header')
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
