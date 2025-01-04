import re


class Validator:

    @staticmethod
    def check_email(email):
        pattern = "^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
        """
        Если в re.match строка соответствует шаблону, то возвращает объект re.match, если нет то None,
        делаем проверку is not None значит вернула объект re.match и email соответствует шаблону
        """
        return re.match(pattern, email) is not None

    @staticmethod
    def check_password(password):
        if len(password) < 5:  # Если пароль меньше 5 символов
            return False
        if not any(p.isdigit() for p in password):  # Если пароль не содержит не одной цифры
            return False
        if not any(i in password for i in '!@#$%^&*()_-+{}[]~'):
            return False
        if not re.search("[!@#$%^&*()_:+{}?/|~]", password):
            return False
        return True









