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


def get_quiz_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1")],
            [KeyboardButton(text="2"), KeyboardButton(text="3")],
            [KeyboardButton(text="4")],
            [KeyboardButton(text="Головне меню")]
        ],
        resize_keyboard=True
    )
    return keyboard

