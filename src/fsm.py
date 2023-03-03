from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    change_pass_length = State()
