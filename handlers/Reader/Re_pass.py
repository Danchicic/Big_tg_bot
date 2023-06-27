from aiogram import Router
from aiogram.filters import Command, Text, CommandStart
from aiogram.types import CallbackQuery, Message
from keyboards import kb
from lexicon.lexicon_ru import lexicon

re_pass_router: Router = Router()


@re_pass_router.message(Text(text='Как начать?'))
async def how_to_start(message: Message):
    await message.answer(
        text=lexicon['как начать'],
        reply_markup=kb.end()
    )


@re_pass_router.message(Text(text='Нет заданий'))
async def no_exes(message: Message):
    await message.answer(
        text=lexicon['нет заданий'],
        reply_markup=kb.end()
    )


@re_pass_router.message(Text(text='Не засчитывается задание'))
async def cant_approve(message: Message):
    await message.answer(text=lexicon['Не засчитывается задание'], reply_markup=kb.end())
