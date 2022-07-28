import sqlite3

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from core.data.__init__ import db
from core.handlers.determine_start_keyboard import determine_keyboad
from core.keyboards.buttons.zodiac_signs_keyboard import zodiac_signs
from core.keyboards.buttons.start_choice_keyboard import start_choice
from core.states.select_zodiac_sign_states import SelectZodiacSign


async def return_zodiacs_keyboard(message: Message):
    if 'Изменить' in message.text and not db.select_user_zodiac_sign(user_id=message.from_user.id)[0]:
        await message.answer(text='Вы не можете <i>изменить</i> свой знак зодиака, поскольку ещё не указали его.')
    elif 'Указать' in message.text and db.select_user_zodiac_sign(user_id=message.from_user.id)[0]:
        await message.answer(text='Вы не можете <i>указать</i> свой знак зодиака, поскольку уже сделали это.')
    else:
        await message.answer(text='Отправьте Ваш знак зодиака.', reply_markup=zodiac_signs)
        await SelectZodiacSign.choice.set()


async def save_zodiac_sign(message: Message, state: FSMContext):
    zodiac_signs_list = [
        'Овен',
        'Телец',
        'Близнецы',
        'Рак',
        'Лев',
        'Дева',
        'Весы',
        'Скорпион',
        'Стрелец',
        'Козерог',
        'Водолей',
        'Рыбы'
    ]

    if message.text == 'Отмена':
        await message.answer(text='Чего бы Вы хотели?', reply_markup=determine_keyboad(message.from_user.id))
        await state.finish()
    elif message.text in zodiac_signs_list:
        try:
            db.update_zodiac_sign(user_id=message.from_user.id, zodiac_sign=message.text)
        except sqlite3.IntegrityError as err:
            print(err)

        await message.answer(text=
                             'Спасибо. Ваш знак зодиака сохранён.'
                             '\nЧего бы Вы хотели ещё?', reply_markup=determine_keyboad(message.from_user.id))
        await state.finish()
    else:
        await message.answer(text='Вы ввели несуществующий знак зодиака, попробуйте ещё раз.')


def register(dp: Dispatcher):
    dp.register_message_handler(callback=return_zodiacs_keyboard, text=['Указать свой знак зодиака',
                                                                        'Изменить свой знак зодиака'])
    dp.register_message_handler(callback=save_zodiac_sign, state=SelectZodiacSign.choice)
