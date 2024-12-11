from flask import Flask
import logging
from flask_wtf import FlaskForm
from werkzeug.exceptions import InternalServerError
from wtforms import IntegerField
from wtforms.validators import InputRequired

app = Flask(__name__)

logger = logging.getLogger(name="divider")

class DivideForm(FlaskForm):
    a = IntegerField(validators=[InputRequired()])
    b = IntegerField(validators=[InputRequired()])

@app.route("/divide/", methods=["POST"])
def divide():
    form = DivideForm()

    if form.validate_on_submit():
        a = form.a.data
        b = form.b.data
        logger.debug(f'Form is valid. a={a}, b={b}')
        return f"a / b = {a / b}", 200
    logger.error(f"Form is not valid. error={form.errors}")
    return f'Bad request', 400

@app.errorhandler(ZeroDivisionError)
def zero(e: ZeroDivisionError):
    logger.exception("Делить на 0 нельзя", exc_info=e)
    return "Деление на 0", 400

@app.errorhandler(InternalServerError)
def error_500(e: InternalServerError):
    original = e.original_exception
    if isinstance(original, Exception):
        print("Тут можно поработать с этой ошибкой")
    return 'Возникла ошибка InternalServerError', 500


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.debug("Started app server")
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(port=5000, debug=True)
