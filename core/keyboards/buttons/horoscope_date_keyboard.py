from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

horoscope_date = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='На сегодня')],
        [KeyboardButton(text='На завтра')],
        [KeyboardButton(text='На неделю')],
        [KeyboardButton(text='Отмена')]
    ],
    resize_keyboard=True
)
