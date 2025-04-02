from aiogram.fsm.state import StatesGroup, State

class SearchEmployee(StatesGroup):
    query = State()