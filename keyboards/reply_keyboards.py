from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔎Шукати вакансії👁"), KeyboardButton(text="📡Анкета📡")],
            [KeyboardButton(text="🔹️️️️️️Перемкнути роль")],
            [KeyboardButton(text="🎮Головне меню")],
        ],
        resize_keyboard=True
    )
    return keyboard


def get_quiz_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📸Поміняти фото📸")],
            [KeyboardButton(text="📊Поміняти текст📊"), KeyboardButton(text="🆙Вибрати Технології/Навички🆙")],
            [KeyboardButton(text="📍Ввести локацію роботи📍"), KeyboardButton(text="💻Описати свій досвід роботи в IT💻")],
            [KeyboardButton(text="❌Видалити анкету❌")],
            [KeyboardButton(text="Головне меню")],
        ],
        resize_keyboard=True
    )
    return keyboard

def get_searchion_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[

            [KeyboardButton(text="😎Запроси друзів – отримай більше лайків 😎"),],
            [KeyboardButton(text="🤖Про нову версію бота🤖")],
            [KeyboardButton(text="Підтримка 24/7📲"), KeyboardButton(text="✏️Про нас✏️") ],
            [KeyboardButton(text="🏢Мій кабінет🏢")]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_workstation_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🕐Моя вакансія🕐"), KeyboardButton(text="👷‍♂️Шукати робітників👷‍♂️")],
            [KeyboardButton(text="🔹️️️️️️Перемкнути роль")],
            [KeyboardButton(text="🎮Головне меню")],
        ],
        resize_keyboard=True
    )
    return keyboard

def get_workstation_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🗄Назва Компанії🗄"), KeyboardButton(text="📥Опис вакансії📥"),],
            [KeyboardButton(text="🔎Кого ви шукаєте🔍"), KeyboardButton(text="💲Зарплатний діпазон💲")],
            [KeyboardButton(text="🗑Видалити анкету🗑") ,KeyboardButton(text="📍Локація компанії🚉")],
            [KeyboardButton(text="Головне меню 💻")]


        ],
        resize_keyboard=True
    )
    return keyboard