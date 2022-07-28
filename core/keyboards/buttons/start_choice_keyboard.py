from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_choice = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Указать свой знак зодиака')],
        [KeyboardButton(text='Посмотреть гороскоп по всем знакам зодиака')]
    ],
    resize_keyboard=True
)

start_choice_registered = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Изменить свой знак зодиака')],
        [
            KeyboardButton(text='Гороскоп на сегодня'),
            KeyboardButton(text='Гороскоп на завтра'),
            KeyboardButton(text='Гороскоп на неделю')
        ],
        [KeyboardButton(text='Посмотреть гороскоп по всем знакам зодиака')]
    ],
    resize_keyboard=True
)
