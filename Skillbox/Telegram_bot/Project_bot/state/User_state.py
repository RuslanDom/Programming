from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    user_id = State()
    type = State()
    year = State()
    genres = State()
    countries = State()
    history = State()
