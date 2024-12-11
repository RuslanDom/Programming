import getpass
import hashlib
import logging

# Создадим объект для логирования введенных данных
logger = logging.getLogger("password_check")

def validator(password: str):
    if not any(i in "!@#$%^&*_+?" for i in password):
        logger.exception("В пароле нет символов")
        return Exception
    elif not any(i.isdigit() for i in password):
        logger.exception("В пароле нет цифр")
        return Exception
    return True

def create_password() -> str or bool:
    logger.debug("Задаём пароль")
    my_admin_pass = getpass.getpass()
    if validator(my_admin_pass) is not Exception:
        hasher = hashlib.md5()
        hasher.update(my_admin_pass.encode('utf-8'))
        result = hasher.hexdigest()
        logger.debug("Пароль успешно сохранён")
        return result
    else:
        logger.warning("Слишком слабый пароль")
    return False


# Функция для проверки пароля с хешированием
def input_and_check_password(old_pass):
    logger.debug('Получаем пароль от пользователя')
    password: str = getpass.getpass()

    if not password:
        logger.warning("Не введён пароль!")
        return False
    try:
        hasher = hashlib.md5()
        hasher.update(password.encode("utf-8"))
        if hasher.hexdigest() == old_pass:
            return True
    except ValueError as ex:
        logger.exception("Некорректный символ", exc_info=ex)

    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)  # Задать уровень логирования
    while True:
        admin_pass = create_password()
        if admin_pass:
            break
    logger.info("Введите пароль")
    count_number: int = 3
    while count_number > 0:
        logger.info(f"Осталось {count_number} попытка(и)")
        if input_and_check_password(admin_pass):
            exit(0)
        count_number -= 1

    logger.error("Пользователь ввёл не верный пароль!")
    exit(1)