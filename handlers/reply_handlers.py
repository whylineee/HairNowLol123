from aiogram import types, Router
from keyboards.inline_keyboards import get_inline_test
from keyboards.reply_keyboards import get_quiz_keyboard, get_main_keyboard

router = Router()


@router.message(lambda message: message.text == "Меню")
async def test_handler(message: types.Message):
    await message.answer("""It's test message!""", reply_markup=get_inline_test())

@router.message(lambda message: message.text == "Анкета")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Ваша анкета""", reply_markup=get_quiz_keyboard())

@router.message(lambda message: message.text == "Головне меню")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Головне меню""", reply_markup=get_main_keyboard())