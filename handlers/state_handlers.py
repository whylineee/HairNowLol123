from aiogram import Router, types
from states.edit_user_states import EditDescUser
from aiogram.fsm.context import FSMContext
from utils.users import edit_field_employee
from states.search_states import SearchEmployee

router = Router()

@router.message(EditDescUser.edit_e_desc)
async def edit_desc_handler(message: types.Message, state: FSMContext):
    await state.update_data(edit_desc=message.text)
    data = await state.get_data()
    msg_text = edit_field_employee(message, "description", data)
    await message.answer(msg_text)
    await state.clear()

@router.message(SearchEmployee.query)
async def SearchEmployee(message: types.Message, state: FSMContext):
    await state.update_data(query=message.text)
    data = await state.get_data()
    print("Querry:", data['query'])
    await state.clear()