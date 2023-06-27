from aiogram.filters.state import State, StatesGroup


class FSMChooseProfile(StatesGroup):
    author = State()
    translator = State()
    reader = State()


