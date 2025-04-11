import json

from aiogram import types, Router
from aiogram.types import FSInputFile

from keyboards.inline_keyboards import get_inline_hs
from keyboards.reply_keyboards import get_quiz_keyboard, get_main_keyboard, get_searchion_keyboard, \
    get_workstation_keyboard, get_workstation_menu_keyboard
from aiogram.fsm.context import FSMContext

from states.change_skills_py import ChangeSkills
from states.company_states.who_search_py import WhoSearch
from states.edit_user_states import EditDescUser
from states.search_states import SearchEmployee
from states.enter_location import EnterLocations
from states.describe_experience import DescribeExperience
from states.company_states.name_company import NameCompany
from states.company_states.describe_vacancy import DesVacancy
from states.company_states.search_company import SearchCompany
from states.company_states.company_locations import LocationsCompany
from states.company_states.salary_comp import SalaryComp
from states.upload_media_states import UploadMediaStates

from utils.users import get_employee_text, get_company_text

router = Router()


@router.message(lambda message: message.text == "🎮Головне меню")
async def test_handler(message: types.Message):
    await message.answer("""Головне меню""", reply_markup=get_searchion_keyboard())


@router.message(lambda message: message.text == "Моя анкета")
async def test_handler(message: types.Message):
    await message.answer("""1. Моя анкета""", reply_markup=get_searchion_keyboard())


@router.message(lambda message: message.text == "🕐Моя вакансія🕐")
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


@router.message(lambda message: message.text == "✏️Про нас✏️")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Цей бот створив : whylineee
    ПІБ: Савин Марко Андрійович""", reply_markup=get_searchion_keyboard())


@router.message(lambda message: message.text == "Підтримка 24/7")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Привіт, це цілодобова підтримка нашого телеграм-боту,
напиши сюди (jpg_junior) і тобі дадуть відповідь.
Дякую за те що користуєшся нашим ботом.""", reply_markup=get_main_keyboard())


@router.message(lambda message: message.text == "Підтримка 24/7📲")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Привіт, це цілодобова підтримка нашого телеграм-боту,
напиши сюди (whylineee) і тобі дадуть відповідь.
Дякую за те що користуєшся нашим ботом.""", reply_markup=get_searchion_keyboard())


@router.message(lambda message: message.text == "📊Поміняти текст📊")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await message.answer("""Введіть новий текст""")
    await state.set_state(EditDescUser.edit_e_desc)


@router.message(lambda message: message.text == "👷‍♂️Шукати робітників👷‍♂️")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await state.set_state(SearchEmployee.query)
    await message.answer("""Ось доступні анкети:""")
    with open("data/employee.json", "r") as f:
        employee = json.load(f)
    for employee in employee:
        text = get_employee_text(employee)
        if employee["profile_img"] is not None:
            photo_file = FSInputFile(employee["profile_img"])
            await message.answer_photo(photo=photo_file, caption=text, reply_markup=get_workstation_keyboard())
        else:
            await message.answer(text, reply_markup=get_workstation_keyboard())


@router.message(lambda message: message.text == "🤖Про нову версію бота🤖")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Привіт, це найновіша версія бота!""", reply_markup=get_searchion_keyboard())


@router.message(lambda message: message.text == "🤖Про нову версію бота🤖")
async def questionnaire_handler(message: types.Message):
    await message.answer("""Привіт, це найновіша версія бота!""", reply_markup=get_searchion_keyboard())


@router.message(lambda message: message.text == "😎Запроси друзів – отримай більше лайків 😎")
async def questionnaire_handler(message: types.Message):
    await message.answer("""ось твій реферальний код""", reply_markup=get_searchion_keyboard())


@router.message(lambda message: message.text == "🆙Вибрати Технології/Навички🆙")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await message.answer("""Впишіть ваші технології""", )
    await state.set_state(ChangeSkills.change_e_skills)


@router.message(lambda message: message.text == "💻Описати свій досвід роботи в IT💻")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await message.answer("""Опишіть ваш досвід:""", )
    await state.set_state(DescribeExperience.describe_e_experience)


@router.message(lambda message: message.text == "📍Ввести локацію роботи📍")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await message.answer("""Введіть локацію:""", )
    await state.set_state(EnterLocations.enter_e_locations)


@router.message(lambda message: message.text == "🏢Мій кабінет🏢" or message.text == "🔹️️️️️️Перемкнути роль")
async def cabinet_handler(message: types.Message):
    await message.answer("""Вибери хто ти, Роботодавець чи працівник?""", reply_markup=get_inline_hs())


@router.message(lambda message: message.text == "🗄Назва Компанії🗄")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await message.answer("""Введіть назву компанії:""", )
    await state.set_state(NameCompany.name_c_company)


@router.message(lambda message: message.text == "📥Опис вакансії📥")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await message.answer("""Введіть опис вакансії:""", )
    await state.set_state(DesVacancy.des_c_vacancy)


@router.message(lambda message: message.text == "🔎Кого ви шукаєте🔍")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await message.answer("""Кого ви шукаєте:""", )
    await state.set_state(WhoSearch.who_c_search)


@router.message(lambda message: message.text == "🔎Шукати вакансії👁")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await state.set_state(SearchCompany.company)
    await message.answer("""Ось доступні вакансії:""")
    with open("data/company.json", "r") as f:
        company = json.load(f)
    for company in company:
        text = get_company_text(company)
        await message.answer(text, reply_markup=get_main_keyboard())


@router.message(lambda message: message.text == "📍Локація компанії🚉")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await message.answer("""Введіть локацію компанії:""", )
    await state.set_state(LocationsCompany.loc_c_company)


@router.message(lambda message: message.text == "💲Зарплатний діпазон💲")
async def questionnaire_handler(message: types.Message, state: FSMContext):
    await message.answer("""Введіть зарплатний діапазон:""", )
    await state.set_state(SalaryComp.salary_comp)


@router.message(lambda message: message.text == "📸Поміняти фото📸")
async def media_handler(message: types.Message, state: FSMContext):
    await state.set_state(UploadMediaStates.wait_for_photo)
    await message.answer("Please sent photo:")
