import hashlib


# ХЕШИРОВАНИЕ ПАРОЛЯ
def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()