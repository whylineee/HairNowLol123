from aiogram import types, Router
from keyboards.  inline_keyboards import get_inline_test

router = Router()


@router.message(lambda message: message.text == "Меню")
async def test_handler(message: types.Message):
    await message.answer("""It's test message!""", reply_markup=get_inline_test())

@router.message(lambda message: message.text == "Анкета")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Ваша анкета""", reply_markup=get_inline_test())