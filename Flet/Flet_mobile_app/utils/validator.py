import re


class Validator:
    def check_email(self, email):
        pattern = r"^[a-zA-Z0-9._+-%]+@[a-zA-Z0-9-.]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return True
        return False

    def check_phone(self, phone):
        pattern = r"^(?:\+7|8)\d{10}$"
        if re.match(pattern, phone):
            return True
        return False

    def check_car_number(self, car_number):
        pattern = r"^[ABCEHKMOPTУX]{1}\d{3}[ABCEHKMOPTУX]{2}\d{2,3}$"
        if re.match(pattern, car_number.upper()):
            return True
        return False

    def check_password(self, password):
        pattern = r"^[A-Za-z0-9+_-!]{4,}$"
        if re.match(pattern, password):
            if not any(p.isdigit() for p in password) or not re.search(r"\+_!-", password):
                return False
            return True
        return False




