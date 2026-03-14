from loguru import logger
from flask import Flask

app = Flask(__name__)


logger.add(
    "logs/log.log",
    rotation='1 week',
    compression='zip',
    encoding='utf-8',
    level='DEBUG',
    format='{time} {level} {message}',
    backtrace=True,
    diagnose=True,
    # serialize=True
)

@app.route('/one')
def one():
    logger.info('route one')
    return 'one', 200

@app.route('/error')
def get_error():
    try:
        null_var = 0
        a = 1/ null_var
    except ZeroDivisionError:
        logger.exception("Error")
    return 'error'

@app.route('/decorator_error')
@logger.catch
def decorator_error():
    null_var = 0
    a = 1/ null_var
    return 'decorator_error'


if __name__ == '__main__':
    app.run(debug=True)



