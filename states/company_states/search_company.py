from aiogram.fsm.state import StatesGroup, State

class SearchCompany(StatesGroup):
    company = State()