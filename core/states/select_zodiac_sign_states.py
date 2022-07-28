from aiogram.dispatcher.filters.state import StatesGroup, State


class SelectZodiacSign(StatesGroup):
    choice = State()
