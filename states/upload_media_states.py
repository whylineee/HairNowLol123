from aiogram.fsm.state import State, StatesGroup

class UploadMediaStates(StatesGroup):
    wait_for_photo = State()