from aiogram import Router, types
import os

from aiogram.types import FSInputFile

from states.edit_user_states import EditDescUser
from aiogram.fsm.context import FSMContext
from utils.users import edit_field_employee, edit_field_company
from states.search_states import SearchEmployee
from states.change_skills_py import ChangeSkills
from states.enter_location import EnterLocations
from states.describe_experience import DescribeExperience
from states.company_states.name_company import NameCompany
from states.company_states.describe_vacancy import DesVacancy
from states.company_states.who_search_py import WhoSearch
from states.company_states.company_locations import LocationsCompany
from states.company_states.salary_comp import SalaryComp
from states.upload_media_states import UploadMediaStates
router = Router()

@router.message(EditDescUser.edit_e_desc)
async def edit_desc_handler(message: types.Message, state: FSMContext):
    await state.update_data(edit_desc=message.text)
    data = await state.get_data()
    msg_text = edit_field_employee(message, "description", {
        "new_value": data['edit_desc'],
    })
    await message.answer(msg_text)
    await state.clear()

@router.message(SearchEmployee.query)
async def query(message: types.Message, state: FSMContext):
    await state.update_data(query=message.text)
    data = await state.get_data()
    print("Query:", data['query'])
    await state.clear()


@router.message(ChangeSkills.change_e_skills)
async def change_e_skills(message: types.Message, state: FSMContext):
    await state.update_data(change_skills=message.text)
    data = await state.get_data()
    # user = message.from_user
    txt = edit_field_employee(message, "skills", {
        "new_value": data['change_skills'],
    })
    await message.answer(txt)
    await state.clear()

@router.message(EnterLocations.enter_e_locations)
async def enter_e_locations(message: types.Message, state: FSMContext):
    await state.update_data(enter_locations=message.text)
    data = await state.get_data()
    print(data['enter_locations'])
    # user = message.from_user
    txt = edit_field_employee(message, "locations", {
        "new_value": data['enter_locations'],
    })
    await message.answer(txt)
    await state.clear()


@router.message(DescribeExperience.describe_e_experience)
async def describe_e_experience(message: types.Message, state: FSMContext):
    await state.update_data(describe_experience=message.text)
    data = await state.get_data()
    # user = message.from_user
    txt = edit_field_employee(message, "experience", {
        "new_value": data['describe_experience'],
    })
    await message.answer(txt)
    await state.clear()


@router.message(UploadMediaStates.wait_for_photo)
async def photo_handler(message: types.Message, state: FSMContext):
    # download photo
    photo = message.photo[-1]
    destination_folder = "media"
    os.makedirs(destination_folder, exist_ok=True)
    file_path = os.path.join(destination_folder, f"{photo.file_unique_id}.jpg")
    file_info = await message.bot.get_file(photo.file_id)
    await message.bot.download_file(file_info.file_path, destination=file_path)

    # write path to employee.json
    saved_photo = edit_field_employee(message, "profile_img", {
        "new_value": file_path
    })
    if saved_photo:
        await message.answer("Photo saved successfully!")

    # send photo use file path
    photo_file = FSInputFile(file_path)
    await message.answer_photo(photo=photo_file, caption="Your photo is here:")

    # clear state
    await state.clear()

########################################################################################################################


@router.message(NameCompany.name_c_company)
async def name_c_company(message: types.Message, state: FSMContext):
    await state.update_data(company_name=message.text)
    data = await state.get_data()
    # user = message.from_user
    txt = edit_field_company(message, "company_name", {
        "new_value": data['company_name'],
    })
    await message.answer(txt)
    await state.clear()


@router.message(DesVacancy.des_c_vacancy)
async def name_c_company(message: types.Message, state: FSMContext):
    await state.update_data(des_vacancy=message.text)
    data = await state.get_data()
    # user = message.from_user
    txt = edit_field_company(message, "description", {
        "new_value": data['des_vacancy'],
    })
    await message.answer(txt)
    await state.clear()

@router.message(WhoSearch.who_c_search)
async def name_c_company(message: types.Message, state: FSMContext):
    await state.update_data(who_search=message.text)
    data = await state.get_data()
    # user = message.from_user
    txt = edit_field_company(message, "search", {
        "new_value": data['who_search'],
    })
    await message.answer(txt)
    await state.clear()


@router.message(LocationsCompany.loc_c_company)
async def name_c_company(message: types.Message, state: FSMContext):
    await state.update_data(enter_c_locations=message.text)
    data = await state.get_data()
    # user = message.from_user
    txt = edit_field_company(message, "locations", {
        "new_value": data['enter_c_locations'],
    })
    await message.answer(txt)
    await state.clear()


@router.message(SalaryComp.salary_comp)
async def name_c_company(message: types.Message, state: FSMContext):
    await state.update_data(enter_salary=message.text)
    data = await state.get_data()
    # user = message.from_user
    txt = edit_field_company(message, "salary", {
        "new_value": data['enter_salary'],
    })
    await message.answer(txt)
    await state.clear()




