from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    name = State()
    lastname = State()
    age = State()