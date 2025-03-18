from aiogram import types, Router

router = Router()

@router.callback_query(lambda c: c.data.startswith("test_btn_"))
async def test_callback_handler(callback_query: types.CallbackQuery):
    data = callback_query.data
    print("______d", data)
    if data == "test_btn_1":
        await callback_query.answer('You pressed first Inline Button')
    elif data == "test_btn_2":
        await callback_query.answer('You pressed second Inline Button')
