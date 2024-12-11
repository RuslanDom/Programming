import getpass
import hashlib
import logging
from concurrent.futures import ProcessPoolExecutor
import asyncio
from asyncio import AbstractEventLoop
from multiprocessing import Process



logger = logging.getLogger("password_checker")

def get_list():
    with open("/usr/share/dict/words", 'r') as file:
        list_words = [word.lower() for word in file.read().split('\n') if len(word) >= 4]
    return list_words


def is_strong_password(password: str) -> bool:
    if password in LIST_WORDS:
        return False
    return True


def input_and_check_password(password) -> bool:
    logger.debug("Начало input_and_check_password")



    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False
    elif is_strong_password(password):
        logger.warning("Вы ввели слишком слабый пароль")
        return False

    try:
        hasher = hashlib.md5()

        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            print(password)
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)

    return False


async def main():
    loop: AbstractEventLoop = asyncio.get_running_loop()
    with ProcessPoolExecutor as pool:
        pass



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    LIST_WORDS = get_list()
    logger.info("Вы пытаетесь аутентифицироваться в Skillbox")
    count_number: int = 3
    logger.info(f"У вас есть {count_number} попыток")

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error("Пользователь трижды ввёл не правильный пароль!")
    exit(1)
