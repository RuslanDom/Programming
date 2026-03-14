from flask import Flask
import time, random
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/index')
def index():
    time.sleep(random.randint(1,5))
    return '''
    <html>
    <head><h1>Основная страница</h1></head>
    <body>
        <h2><em>Главная страница</em></h2>
    </body>
    </html>
    '''

@app.route('/one')
def one():
    return 'one ok', 200

@app.route('/two')
def two():
    return 'two ok', 200

@app.route('/about')
def about():
    time.sleep(random.randint(1,5))
    return '''
    <html>
    <body>
        <h2>О нас</h2>
    </body>
    </html>
    '''


@app.route('/error')
def error():
    return ':(', 500


if __name__ == '__main__':
    app.run(debug=False)


# from flask import Flask
# from prometheus_flask_exporter import PrometheusMetrics
#
# app = Flask(__name__)
# metrics = PrometheusMetrics(app)
#
# @app.route('/')
# def src():
#     return 'OK'
#
# if __name__ == '__main__':
#     app.run(debug=False)