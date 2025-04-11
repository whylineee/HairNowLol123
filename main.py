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
from keyboards.reply_keyboards import get_main_keyboard, get_searchion_keyboard
from keyboards.inline_keyboards import get_inline_hs
from handlers import register_handlers
from utils.users import add_new_employee
from utils.users import add_new_company


# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()
register_handlers(dp)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привіт, {html.bold(message.from_user.full_name)}!\n"
                         "HireNow – бот для пошуку роботи в IT-сфері.", reply_markup=get_searchion_keyboard())
    await message.answer(f"Він допомагає працівникам знайти вакансії за їхніми навичками, а роботодавцям – швидко знаходити кваліфікованих спеціалістів. "
                         "Вибери хто ти, Роботодавець чи працівник?",
                         reply_markup=get_inline_hs())


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
