from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Меню")],
            [KeyboardButton(text="Анкета"), KeyboardButton(text="Меню")],
            [KeyboardButton(text="Меню")]
        ],
        resize_keyboard=True
    )
    return keyboard




