from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Напишите кодовое слово и получите свой приз', reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_start(message: Message):
    await message.answer('Напишите кодовое слово и получите свой приз')


@router.message(F.text == 'ГЫ')
async def cmd_start(message: Message):
    await message.answer('Не ГЫкай')


@router.message(F.photo)
async def cmd_start(message: Message):
    await message.answer(f'ID photo: {message.photo[-1].file_id}')


@router.message(Command('get_photo'))
async def cmd_start(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAMiZgl_u2gIK_f2HID8QIxy-VJBM20AAi_fMRvh50hIW9erwpm3nXABAAMCAAN4AAM0BA',
        caption='фото')
