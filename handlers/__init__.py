from aiogram import Dispatcher
from .reply_handlers import router as reply_router
from .inline_handlers import router as inline_router


def register_handlers(dp: Dispatcher):
    dp.include_router(reply_router)
