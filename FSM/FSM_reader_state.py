from aiogram.filters.state import State, StatesGroup


class FSMReaderAnswer(StatesGroup):
    wait24 = State()
    link_re = State()
    linked = State()
