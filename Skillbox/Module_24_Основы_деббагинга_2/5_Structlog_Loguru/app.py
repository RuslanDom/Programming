import structlog
from structlog.stdlib import LoggerFactory
from flask import Flask, request, g
import logging, sys
import datetime

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='%(levelname)s - %(message)s'
)

app = Flask(__name__)

structured_log = structlog.get_logger()

def timestamper(_, __, event_dict):
    event_dict['time'] = datetime.datetime.now().isoformat()
    return event_dict

structlog.configure(
    processors=[timestamper, structlog.processors.JSONRenderer()],  # Записывает логи в формате json
    logger_factory=LoggerFactory()  # Для синхры с базовым логгером logging
)

@app.before_request
def before_request():
    method = request.method
    user_agent = request.user_agent
    log = structured_log.bind(method=method, user_agent=user_agent)
    g.log = log

@app.route('/one')
def one():
    g.log.msg("route one")
    return 'one', 200

@app.route('/two')
def two():
    g.log.msg("route two")
    return 'two', 200


if __name__ == '__main__':
    app.run()
