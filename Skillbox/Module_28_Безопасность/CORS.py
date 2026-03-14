from flask import Flask, jsonify, request, Response, g
import sqlite3
import requests
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

def get_db() -> sqlite3.Connection:
    connection = getattr(g, '_database', None)
    if connection is None:
        connection = g._database = sqlite3.connect('mR.db')
    return connection

@app.before_request
def create_table():
    with sqlite3.connect('mR.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS myRequests (id INTEGER PRIMARY KEY AUTOINCREMENT, ip_address VARCHAR(50))
            """
        )
        conn.commit()

@app.teardown_appcontext
def close_connection(exception):
    conn = get_db()
    if conn is not None:
        conn.close()


@app.route('/', methods=['GET'])
def index():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO myRequests (ip_address) VALUES (?)""", (client_ip,))
    conn.commit()
    return jsonify({"status": "SUCCESS"})

@app.route("/data", methods=['GET'])
def get_data():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM myRequests""")
    data = cursor.fetchall()
    print(data)
    resp = list(map(lambda x: x[1], data))
    return jsonify(resp)


# Другой способ разрешить для всех endpoint отправлять запросы с другого источника
@app.after_request
def after_request(response: Response) -> Response:
    # response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)


