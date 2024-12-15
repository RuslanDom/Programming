from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):  # Обязательно наследуется класс StatesGroup
    # Все аргументы должны быть объектами класса State()
    name = State()
    age = State()
    country = State()
    city = State()
    phone_number = State()
