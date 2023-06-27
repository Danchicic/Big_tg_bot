from aiogram import Router
from aiogram.filters import StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from FSM.fsm_default_state import FSMChooseProfile
from keyboards import kb
from keyboards.reader_kb import start_reader
from aiogram.filters.state import State, StatesGroup

main_router: Router = Router()
main_router.message.filter(StateFilter(FSMChooseProfile.reader))
main_router.message.

@main_router.message(Text(text='Re:pass'))
async def re_pass(message: Message, state: FSMContext):
    await state.update_data(reader=(1, start_reader))

    await message.answer(
        text='Выберите ваш вопрос',
        reply_markup=kb.create_kb('Как начать?', 'Нет заданий', 'Не засчитывается задание')
    )


@main_router.message(Text(text='Вопросы по переводу'))
async def questions_translation(message: Message, state: FSMContext):
    await message.answer(
        text='Выберите ваш вопрос',
        reply_markup=kb.create_kb('Качество перевода', 'Переводчики не открывают платки'))


@main_router.message(Text(text='У меня возникла ошибка'))
async def error(message: Message, state: FSMContext):
    await message.answer(
        text='Выберите ваш вопрос',
        reply_markup=kb.create_kb('Ошибка 404', 'Ошибка 500', 'Не грузятся картинки', 'Я нашел баг')
    )


@main_router.message(Text(text='Другое'))
async def another(message: Message, state: FSMContext):
    await message.answer(
        text='Выберите ваш вопрос',
        reply_markup=kb.create_kb('Хочу предложить фичу', 'Мне дали бан', 'Позвать модератора')
    )


@main_router.message(Text(text='Не пришли деньги/тикеты'))
async def no_money(message: Message, state: FSMContext):
    await message.answer(
        text='Выберите ваш вопрос',
        reply_markup=kb.create_kb('Не пришли деньги', 'Не пришли тикеты')
    )
