import hashlib
import string
import random

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Функция для генерации случайных имён файлов
def p_link_generate(length: int) -> str:
    letters_and_digits = string.ascii_letters + string.digits
    result_str = "".join(random.choice(letters_and_digits) for _ in range(length))
    return result_str

