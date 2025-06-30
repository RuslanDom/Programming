import re

class Validator:
    def  email_valid(self, email):
        """
        Функция проверки email
        """
        pattern = "^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
        return not re.match(pattern=pattern, string=email)

    def password_valid(self, password):
        """
        Функция проверки пароля
        """
        pattern = "[!@_#№$%&?]"
        if len(password) < 8:
            return True
        if not any(p.isdigit() for p in password):
            return True
        if not re.search(pattern=pattern, string=password):
            return True

    def time_valid(self, time):
        """
        Функция проверки времени
        """
        pattern = r"^[0-2]\d{1}:[0-5]\d{1}$"
        return re.match(pattern=pattern, string=time)