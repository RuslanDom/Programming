import logging.config
from typing import Optional

from flask import Flask
from flask_wtf import FlaskForm
from werkzeug.exceptions import InternalServerError
from wtforms.fields.numeric import IntegerField
from wtforms.validators import InputRequired
from logger_setup import dict_config

from worker1 import worker1
from worker2 import worker2
from worker3 import worker3

app = Flask(__name__)

logging.config.dictConfig(dict_config)
logger = logging.getLogger('main')

class WorkerForm(FlaskForm):
    x = IntegerField(validators=[InputRequired()])
    y = IntegerField(validators=[InputRequired()])

@app.route("/worker1", methods=["POST"])
def _worker1_endpoint():
    form = WorkerForm()

    if form.validate_on_submit():
        x, y = form.x.data, form.y.data
        result = worker1(x, y)
        return f"{x} ** {y} = {result}"
    logger.error(f"Cannot process form {form.errors}")

    return "Cannot process form", 400


@app.route("/worker2", methods=["POST"])
def _worker2_endpoint():
    form = WorkerForm()

    if form.validate_on_submit():
        x, y = form.x.data, form.y.data
        result = worker2(x, y)
        return f"{x} ** {y} = {result}"
    logger.error(f"Cannot process form {form.errors}")

    return "Cannot process form", 400


@app.route("/worker3", methods=["POST"])
def _worker3_endpoint():
    form = WorkerForm()

    if form.validate_on_submit():
        x, y = form.x.data, form.y.data
        result = worker3(x, y)
        return f"{x} ** {y} = {result}"
    logger.error(f"Cannot process form {form.errors}")

    return "Cannot process form", 400


@app.errorhandler(InternalServerError)
def handle_exception(e: InternalServerError):
    # original: Optional[Exception] = getattr(e, "original_exception", None)
    #
    # if original:
    #     logger.exception("Handler uncaught exception", exc_info=original)
    #
    # return "InternalServerError", 500
    logger.exception(e)
    return "InternalServerError", 500

if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)


# curl -X POST http://127.0.0.1:5000/worker1 --data "x=2&y=2"    с ошибкой
# curl -X POST http://127.0.0.1:5000/worker1 --data "x=1&y=2"    без ошибки
