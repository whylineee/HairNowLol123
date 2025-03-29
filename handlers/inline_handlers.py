from aiogram import types, Router
from keyboards.reply_keyboards import get_main_keyboard, get_workstation_keyboard
router = Router()

@router.callback_query(lambda c: c.data.startswith("test_btn_"))
async def test_callback_handler(callback_query: types.CallbackQuery):
    data = callback_query.data
    print("______d", data)
    if data == "test_btn_1":
        await callback_query.message.answer('Ти нажав на кнопку "Працівник", Дякую за те що користуєшся нашим ботом', reply_markup=get_main_keyboard())
    elif data == "test_btn_2":
        await callback_query.message.answer('Ти нажав на кнопку "Роботодавець", Дякую за те що користуєшся нашим ботом', reply_markup=get_workstation_keyboard())
