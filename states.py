from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    group = State()
    chane_group = State()
    dialog = State()