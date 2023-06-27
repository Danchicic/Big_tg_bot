from aiogram import Router
from aiogram.filters import Command, Text, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from FSM.fsm_default_state import FSMChooseProfile
from keyboards import kb
from keyboards.kb import start
from lexicon.lexicon_ru import lexicon

user_router: Router = Router()


@user_router.message(Command(commands='change'))
async def start_message(message: Message):
    await message.answer(
        text='Выберите пользователя',
        reply_markup=kb.create_kb('Переводчик', 'Читатель', 'Автор')
    )


@user_router.message(Command(commands='start'))
async def start_message(message: Message):
    await message.answer(
        text='Выберите пользователя',
        reply_markup=kb.create_kb('Переводчик', 'Читатель', 'Автор')
    )


@user_router.message(Command(commands='back'))
async def start_message(message: Message, state: FSMContext):
    stack = await state.get_data()
    for i, (k, v) in enumerate(stack.items()):
        text_to_send, kb_to_send = lexicon[k], v[1]
        print(text_to_send, kb_to_send)
        if i != len(stack) - 1:
            stack = {k: v}
        else:
            text_to_send = lexicon[k]
            kb_to_send = v[1]
        print(i)
    # print(text_to_send, '---', kb_to_send)
    # ПРО фиксировать че происходит и плюс похоже нужно все в один словарь пихать,все фразы из одной фракции
    await message.answer(
        text=text_to_send,
        reply_markup=kb_to_send
    )
    print('new b', stack)


@user_router.message(Text(text='Читатель'), StateFilter(default_state))
async def reader_message(message: Message, state: FSMContext):
    await state.update_data(choose_user=(0, start()))

    await message.answer(
        text='Выберите команду',
        reply_markup=kb.create_kb('Re:pass', 'Вопросы по переводу', 'У меня возникла ошибка', 'Другое')
    )
    await state.set_state(FSMChooseProfile.reader)


# two more handlers and states
@user_router.message(Text(text='У вас остались вопросы?'))
async def end_message(message: Message, state: FSMContext):
    await message.answer(
        text='Выберите пользователя',
        reply_markup=kb.create_kb('Переводчик', 'Читатель', 'Автор')
    )
    await state.clear()
