from aiogram.fsm.state import StatesGroup, State


class Search(StatesGroup):
    answer = State()

