import logging
from flask import Flask
import csv
from werkzeug.exceptions import InternalServerError

app = Flask(__name__)

logger = logging.getLogger(name="bank_id")


@app.route('/bank_api/<branch>/<int:person_id>')
def bank_id(branch: str, person_id: int):
    branch_card_file_name = f"bank_data/{branch}.csv"
    try:
        with open(branch_card_file_name, 'r') as fi:
            csv_reader = csv.DictReader(fi, delimiter=',')

            for record in csv_reader:
                if int(record["id"]) == person_id:
                    logger.info(f"Работник с ID {person_id}: {record["name"]}")
                    return record["name"]
            else:
                logger.warning("Неправильно выполненный запрос на работника")
                return "Person not found", 400
    except FileNotFoundError as er:
        logger.exception("Файл не найден. Status code 500", exc_info=er)



"--------------------------------------------**************************--------------------------------------------"


# Обработка 500 ошибки (ошибка сервера возникает когда есть не обработанные в коде ошибки)
@app.errorhandler(InternalServerError)
def handler_exception_for_bank(e: InternalServerError):
    original = e.original_exception

    if isinstance(original, FileNotFoundError):
        logger.error(f"Tried to access {original.filename}. Exception info {original.strerror}")

    elif isinstance(original, OSError):
        logger.error(f"Unable to access a card. Exception info {original.strerror}")

    return "Internal Server Error", 500


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename='banking.log',
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    app.run()
