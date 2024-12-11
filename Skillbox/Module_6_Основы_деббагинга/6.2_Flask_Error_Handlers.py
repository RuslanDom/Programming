import csv
from typing import Optional
import logging
from flask import Flask
from flask_wtf import FlaskForm
from werkzeug.exceptions import InternalServerError
from wtforms.fields.numeric import IntegerField
from wtforms.validators import InputRequired

# POST запрос через cmd: 'curl -X POST http://localhost:5000/divide/ --data "a=5&b=1"'
# POST запрос через cmd: 'curl -X POST http://localhost:5000/summa/ --data "a=5&b=1"'

app = Flask(__name__)
"--------------------------------------------**************************--------------------------------------------"
# Деление
class DivideForm(FlaskForm):
    a = IntegerField(validators=[InputRequired()])
    b = IntegerField(validators=[InputRequired()])


@app.route("/divide/", methods=["POST"])
def divide():
    form = DivideForm()

    if form.validate_on_submit():
        a, b = form.a.data, form.b.data
        return f"a / b = {a / b:.2f}"
    return f"Bad request. Error = {form.errors}", 400

# Обработка ошибки деления на ноль через Flask
@app.errorhandler(ZeroDivisionError)
def handler_exception(e: ZeroDivisionError):
    return 'На ноль делить нельзя'

"--------------------------------------------**************************--------------------------------------------"
# Подсчёт суммы
class SummaForm(FlaskForm):
    a = IntegerField(validators=[InputRequired()])
    b = IntegerField(validators=[InputRequired()])


@app.route('/summa/', methods=["POST"])
def summa_ab():
    form = SummaForm()

    if form.validate_on_submit():
        a = form.a.data
        b = form.b.data
        return f'Сумма a и b равна {a + b}', 200
    return f'Ошибка: {form.errors}', 400




"--------------------------------------------**************************--------------------------------------------"
# Перепишите банковский endpoint, заменив запись сообщений в файл на логирование. Проверьте работу endpoint-а.
logger = logging.getLogger(name="bank_id")
@app.route('/bank_api/<branch>/<int:person_id>')
def bank_id(branch:str, person_id: int):
    branch_card_file_name = f"bank_data/{branch}.csv"
    try:
        with open(branch_card_file_name, 'r') as fi:
            csv_reader = csv.DictReader(fi, delimiter=',')

            for record in csv_reader:
                if int(record["id"]) == person_id:
                    with open("lod_file.log", 'a') as file:
                        file.write(f"Запрос к базе данных ветка {branch} -- Получение работника по ID: {person_id} -- результат: {record["name"]}\n")
                    logger.info(f"Работник с ID {person_id}: {record["name"]}")
                    return record["name"]
            else:
                with open("lod_file.log", 'a') as file:
                    file.write(f'Неправильно выполненный запрос на работника bank_api/{branch}/{person_id}\n')
                logger.warning("Неправильно выполненный запрос на работника")
                return "Person not found", 400
    except FileNotFoundError as er:
        logger.exception("Файл не найден. Status code 500", exc_info=er)
        with open("lod_file.log", 'a') as err:
            err.write(
                f"Tried to access {er.filename}. Exception info: {er.strerror}\n"
            )


"--------------------------------------------**************************--------------------------------------------"

# Обработка 500 ошибки (ошибка сервера возникает когда есть не обработанные в коде ошибки)
@app.errorhandler(InternalServerError)
def handler_exception_for_bank(e: InternalServerError):
    # У класса InternalServerError есть поле "original_exception"
    # при помощи которого можно понять что за исключение возникло, обращение через getattr для старых версий Flask
    # в новых версиях можно просто так: original = e.original_exception
    original: Optional[Exception] = getattr(e, "original_exception", None)


    if isinstance(original, FileNotFoundError):
        with open("lod_file.log", 'a') as err:
            err.write(
                f"Tried to access {original.filename}. Exception info: {original.strerror}\n"
            )

    elif isinstance(original, OSError):
        with open("lod_file.log", 'a') as err:
            err.write(
                f"Unable to access a card. Exception info: {original.strerror}\n"
            )
        logger.exception("Ошибка 500", exc_info=e.original_exception)

    return "Internal Server Error", 500



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(port=5000, debug=True)






















