import logging
import random
from logging.config import dictConfig
from config import dict_config

logging.config.dictConfig(dict_config)
logger = logging.getLogger("main")


def func():
    logger.debug("Start working...")
    num1 = random.randint(1, 100)
    logger.info(f"Random number №1 = {num1}")
    num2 = random.randint(0, 2)
    logger.info(f"Random number №2 = {num2}")
    logger.debug("Calculation...")
    try:
        result = num1 / num2
        logger.info(f"Result: {result}")
    except ZeroDivisionError as e:
        logger.error("Get error ZeroDivision")
    logger.debug('End working')


if __name__ == "__main__":
    func()
