import json
import logging
import os
from flask import Flask

app = Flask(__name__)
logger = logging.getLogger("account_book")

current_dir = os.path.dirname(os.path.abspath(__file__))
fixtures_dir = os.path.join(current_dir, "fixtures")

departments = {"IT": "it_dept", "PROD": "production_dept"}

@app.route("/account/<department>/<int:account_number>/")
def sort_endpoint(department: str, account_number: int):
   dept_directory_name = departments.get(department)

   if dept_directory_name is None:
      logger.warning("Department not found")
      return "Department not found", 404
   logger.info("Получение департамента прошло успешно!")
   full_department_path = os.path.join(fixtures_dir, dept_directory_name)

   account_data_file = os.path.join(full_department_path, f"{account_number}.json")

   try:
      with open(account_data_file, "r") as fi:
         account_data_txt = fi.read()
   except FileNotFoundError as err:
      logger.exception("Такого аккаунта не существует", exc_info=err)
      return "Такого аккаунта не существует"
   logger.info("Получение аккаунта сотрудника прошло успешно!")
   account_data_json = json.loads(account_data_txt)
   try:
      name, birth_date = account_data_json["name"], account_data_json["birth_date"]
      day, month, year = birth_date.split(".")
      # day, month, _ = birth_date.split(".") Если год не нужен то можно именованную переменную заменить на _
      return f"{name} was born on {day}.{month}.{year}"
   except KeyError as err:
      logger.exception("Ошибка в базе данных! Данные повреждены!", exc_info=err)
      return "Ошибка в базе данных! Данные повреждены!"
   finally:
      logger.info("Завершение работы...")


if __name__ == "__main__":
   logging.basicConfig(level=logging.INFO)
   logger.info("Started account server")
   app.run(debug=True)

# Запрос пример: http://127.0.0.1:5000/account/IT/2/