from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start():
    builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    buttons: list[KeyboardButton] = [KeyboardButton(text='Переводчик'), KeyboardButton(text='Читатель'),
                                     KeyboardButton(text='Автор')]
    builder.row(*buttons)
    return builder.as_markup(resize_keyboard=True)


def end():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='У вас остались вопросы?')]], resize_keyboard=True)


def create_kb(*args: str, width: None | int = 8):
    builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    buttons: list[KeyboardButton] = [KeyboardButton(text=text) for text in args]
    builder.row(*buttons, width=width)
    return builder.as_markup(resize_keyboard=True)
