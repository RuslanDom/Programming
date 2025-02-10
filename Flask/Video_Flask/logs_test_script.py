from logging.config import dictConfig
import logging
from utils.logger_config import dict_config



logger = logging.getLogger("main")
logging.config.dictConfig(dict_config)
logger.setLevel("DEBUG")



def summa(a, b):
    logger.debug(f"a = {a}")
    logger.debug(f"b = {b}")
    try:
        res = a / b
        logger.debug(f"Result = {res}")
        return res
    except ZeroDivisionError as e:
        logger.error("Деление на ноль", exc_info=e)


if __name__ == "__main__":
   print(summa(9, 3))





