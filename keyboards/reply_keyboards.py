from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎮Меню🎮")],[KeyboardButton(text="Шукати вакансію")],
            [KeyboardButton(text="📡Анкета📡"), KeyboardButton(text="Про нас")],
            [KeyboardButton(text="Підтримка 24/7")]
        ],
        resize_keyboard=True
    )
    return keyboard


def get_quiz_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1. Поміняти фото")],
            [KeyboardButton(text="2. Поміняти текст"), KeyboardButton(text="3. Вибрати Технології/Навички")],
            [KeyboardButton(text="4. Вибрати Локацію роботи"), KeyboardButton(text="5. Описати свій досвід роботи в IT ")],
            [KeyboardButton(text="Головне меню")],
        ],
        resize_keyboard=True
    )
    return keyboard

def get_searchion_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[

            [KeyboardButton(text="1. Запроси друзів – отримай більше лайків 😎 "),],
            [KeyboardButton(text="2. Поміняти мову"), KeyboardButton(text="3. Про нову версію бота")],
            [KeyboardButton(text="Головне меню")]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_workstation_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Моя вакансія")],
            [KeyboardButton(text="Шукати робітників")],
            [KeyboardButton(text="Про нас✏️"), KeyboardButton(text="Підтримка 24/7📲"),],
            [KeyboardButton(text="Запроси друзів – отримай більше лайків 😎"), KeyboardButton(text="Про нову версію бота")],
        ],
        resize_keyboard=True
    )
    return keyboard

def get_workstation_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1. Назва Компанії"), KeyboardButton(text="2. Опис вакансії"),],
            [KeyboardButton(text="3. Кого ви шукаєте "), KeyboardButton(text="4. Зарплатний діпазон")],
            [KeyboardButton(text="Головне меню 💻")]


        ],
        resize_keyboard=True
    )
    return keyboard