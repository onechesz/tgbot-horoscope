from aiogram.dispatcher.filters.state import StatesGroup, State


class ShowHoroscope(StatesGroup):
    zodiac_choice = State()
    date_choice = State()
