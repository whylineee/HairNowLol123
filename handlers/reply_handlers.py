from aiogram import types, Router
from keyboards.inline_keyboards import get_inline_test
from keyboards.reply_keyboards import get_quiz_keyboard, get_main_keyboard, get_searchion_keyboard


router = Router()


@router.message(lambda message: message.text == "Меню")
async def test_handler(message: types.Message):
    await message.answer("""Головне меню""", reply_markup=get_searchion_keyboard())

@router.message(lambda message: message.text == "Анкета")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Ваша анкета""", reply_markup=get_quiz_keyboard())

@router.message(lambda message: message.text == "Головне меню")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Головне меню""", reply_markup=get_main_keyboard())

@router.message(lambda message: message.text == "Про нас")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Цей бот створив : whylineee
    ПІБ: Савин Марко Андрійович""", reply_markup=get_main_keyboard())

@router.message(lambda message: message.text == "Підтримка 24/7")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Привіт, це цілодобова підтримка нашого телеграм-боту,
напиши сюди (jpg_junior) і тобі дадуть відповідь.
Дякую за те що користуєшся нашим ботом.""", reply_markup=get_main_keyboard())