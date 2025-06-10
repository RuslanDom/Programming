import re

class Validator:
    def  email_valid(self, email):
        pattern = "^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
        return not re.match(pattern=pattern, string=email)

    def password_valid(self, password):
        pattern = "[!@_#№$%&?]"
        if len(password) < 8:
            return True
        if not any(p.isdigit() for p in password):
            return True
        if not re.search(pattern=pattern, string=password):
            return True

