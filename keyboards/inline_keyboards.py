from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_hs() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Працівник", callback_data="test_btn_1"),
         InlineKeyboardButton(text="Роботодавець", callback_data="test_btn_2")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)



