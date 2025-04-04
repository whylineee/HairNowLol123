import json

from aiogram import types, Router

from keyboards.inline_keyboards import get_inline_hs
from keyboards.reply_keyboards import get_quiz_keyboard, get_main_keyboard, get_searchion_keyboard, \
    get_workstation_keyboard, get_workstation_menu_keyboard
from aiogram.fsm.context import FSMContext

from states.change_skills_py import ChangeSkills
from states.edit_user_states import EditDescUser
from states.search_states import SearchEmployee

from utils.users import get_employee_text

router = Router()


@router.message(lambda message: message.text == "🎮Головне меню")
async def test_handler(message: types.Message):
    await message.answer("""Головне меню""", reply_markup=get_searchion_keyboard())


@router.message(lambda message: message.text == "Моя анкета")
async def test_handler(message: types.Message):
    await message.answer("""1. Моя анкета""", reply_markup=get_searchion_keyboard())


@router.message(lambda message: message.text == "Моя вакансія")
async def test_handler(message: types.Message):
    await message.answer("""Ваша вакансія""", reply_markup=get_workstation_menu_keyboard())


@router.message(lambda message: message.text == "Про нас")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Цей бот створив : whylineee
    ПІБ: Савин Марко Андрійович""", reply_markup=get_main_keyboard())


@router.message(lambda message: message.text == "📡Анкета📡")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Ваша анкета""", reply_markup=get_quiz_keyboard())


@router.message(lambda message: message.text == "Головне меню")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Головне меню""", reply_markup=get_main_keyboard())


@router.message(lambda message: message.text == "Головне меню 💻")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Головне меню""", reply_markup=get_workstation_keyboard())


@router.message(lambda message: message.text == "Про нас✏️")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Цей бот створив : whylineee
    ПІБ: Савин Марко Андрійович""", reply_markup=get_workstation_keyboard())


@router.message(lambda message: message.text == "Підтримка 24/7")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Привіт, це цілодобова підтримка нашого телеграм-боту,
напиши сюди (jpg_junior) і тобі дадуть відповідь.
Дякую за те що користуєшся нашим ботом.""", reply_markup=get_main_keyboard())


@router.message(lambda message: message.text == "Підтримка 24/7📲")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Привіт, це цілодобова підтримка нашого телеграм-боту,
напиши сюди (jpg_junior) і тобі дадуть відповідь.
Дякую за те що користуєшся нашим ботом.""", reply_markup=get_workstation_keyboard())


@router.message(lambda message: message.text == "2. Поміняти текст")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await message.answer("""Введіть новий текст""")
    await state.set_state(EditDescUser.edit_e_desc)


@router.message(lambda message: message.text == "Шукати робітників")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await state.set_state(SearchEmployee.query)
    await message.answer("""Ось доступні анкети:""")
    with open("data/employee.json", "r") as f:
        employee = json.load(f)
    for employee in employee:
        text = get_employee_text(employee)
        await message.answer(text, reply_markup=get_workstation_keyboard())


@router.message(lambda message: message.text == "Про нову версію бота")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Привіт, це найновіша версія бота!""", reply_markup=get_workstation_keyboard())


@router.message(lambda message: message.text == "3. Про нову версію бота")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Привіт, це найновіша версія бота!""", reply_markup=get_searchion_keyboard())


@router.message(lambda message: message.text == "1. Запроси друзів – отримай більше лайків 😎 ")
async def questionnaire_handler(message: types.Message):
    await message.answer("""ось твій реферальний код""", reply_markup=get_searchion_keyboard())


@router.message(lambda message: message.text == "3. Вибрати Технології/Навички")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await message.answer("""Впишіть ваші технології""", )
    await state.set_state(ChangeSkills.change_e_skills)


@router.message(lambda message: message.text == "😎Мій кабінет" or message.text == "🔹️️️️️️Перемкнути роль")
async def cabinet_handler(message: types.Message):
    await message.answer("""Вибери хто ти, Роботодавець чи працівник?""", reply_markup=get_inline_hs())
