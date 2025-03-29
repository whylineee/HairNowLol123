import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# keyboards
from keyboards.reply_keyboards import get_main_keyboard
from keyboards.inline_keyboards import get_inline_hs
from handlers import register_handlers
from utils.users import add_new_employee

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()
register_handlers(dp)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привіт, {html.bold(message.from_user.full_name)}!"


                         "  HairNow – бот для пошуку роботи в IT-сфері."
                         "       Він допомагає працівникам знайти вакансії за їхніми навичками, а роботодавцям – швидко знаходити кваліфікованих спеціалістів. "
                         "                                                           Вибери хто ти, Роботодавець чи працівник?",
                         reply_markup=get_inline_hs())

    add_new_employee(message.from_user)


# @dp.message()
# async def echo_handler(message: Message) -> None:
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
