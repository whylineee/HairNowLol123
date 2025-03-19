from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Меню")],
            [KeyboardButton(text="Анкета"), KeyboardButton(text="Зв'язатись з нами")],
            [KeyboardButton(text="Підтримка 24/7")]
        ],
        resize_keyboard=True
    )
    return keyboard


def get_quiz_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1. Поміняти фото")],
            [KeyboardButton(text="2. Поміняти текст"), KeyboardButton(text="3")],
            [KeyboardButton(text="4")],
            [KeyboardButton(text="Головне меню")]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_searchion_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1. Поміasdfs")],
            [KeyboardButton(text="2. Помінddяти текст"), KeyboardButton(text="3sdfs")],
            [KeyboardButton(text="4sdf")],
            [KeyboardButton(text="Головне меню")]
        ],
        resize_keyboard=True
    )
    return keyboard