from aiogram import Router, types
from states.edit_user_states import EditDescUser
from aiogram.fsm.context import FSMContext
from utils.users import edit_field_employee
from states.search_states import SearchEmployee
from states.change_skills_py import ChangeSkills

router = Router()

@router.message(EditDescUser.edit_e_desc)
async def edit_desc_handler(message: types.Message, state: FSMContext):
    await state.update_data(edit_desc=message.text)
    data = await state.get_data()
    msg_text = edit_field_employee(message, "description", data)
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
    user = message.from_user
    print("___data", data)
    print("___user", user)
    await state.clear()
