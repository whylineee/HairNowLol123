from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Меню")],
            [KeyboardButton(text="Анкета"), KeyboardButton(text="Про нас")],
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
            [KeyboardButton(text="6. Вибрати напрямок розробки "),  KeyboardButton(text="7. Вибрати зарплатний діапазон")],
            [KeyboardButton(text="Головне меню")],
        ],
        resize_keyboard=True
    )
    return keyboard

def get_searchion_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1. Моя анкета")],
            [KeyboardButton(text="2. Запроси друзів – отримай більше лайків 😎 "),],
            [KeyboardButton(text="3. Поміняти мову"), KeyboardButton(text="4. Про нову версію бота")],
            [KeyboardButton(text="Головне меню")]
        ],
        resize_keyboard=True
    )
    return keyboard