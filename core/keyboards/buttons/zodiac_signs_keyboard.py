from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

zodiac_signs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Овен'),
            KeyboardButton(text='Весы')
        ],
        [
            KeyboardButton(text='Телец'),
            KeyboardButton(text='Скорпион')
        ],
        [
            KeyboardButton(text='Близнецы'),
            KeyboardButton(text='Стрелец')
        ],
        [
            KeyboardButton(text='Рак'),
            KeyboardButton(text='Козерог')
        ],
        [
            KeyboardButton(text='Лев'),
            KeyboardButton(text='Водолей')
        ],
        [
            KeyboardButton(text='Дева'),
            KeyboardButton(text='Рыбы')
        ],
        [
            KeyboardButton(text='Отмена')
        ]
    ],
    resize_keyboard=True
)
