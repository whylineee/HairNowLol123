from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_test() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="test1", callback_data="test_btn_1"),
         InlineKeyboardButton(text="test2", callback_data="test_btn_2")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
