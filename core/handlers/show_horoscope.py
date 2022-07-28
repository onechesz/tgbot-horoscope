import asyncio

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from core.handlers.determine_start_keyboard import determine_keyboad
from core.keyboards.buttons.horoscope_date_keyboard import horoscope_date
from core.keyboards.buttons.zodiac_signs_keyboard import zodiac_signs
from core.parsers.horoscope import horoscope as horoscope_all
from core.states.show_horoscope_states import ShowHoroscope


async def return_zodiacs_keyboard(message: Message):
    await message.answer(text='Выберите знак зодиака, для которого Вы хотите посмотреть гороскоп.',
                         reply_markup=zodiac_signs)
    await ShowHoroscope.zodiac_choice.set()


async def return_date_keyboard(message: Message, state: FSMContext):
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
        async with state.proxy() as data:
            data['zodiac_sign'] = message.text

        await message.answer(text='Выберите дату гороскопа.', reply_markup=horoscope_date)
        await ShowHoroscope.date_choice.set()
    else:
        await message.answer(text='Вы ввели несуществующий знак зодиака. Попробуйте ещё раз.')


async def return_horoscope(message: Message, state: FSMContext):
    dates = [
        'На сегодня',
        'На завтра',
        'На неделю'
    ]
    data = await state.get_data()

    if message.text == 'Отмена':
        await message.answer(text='Чего бы Вы хотели?', reply_markup=determine_keyboad(message.from_user.id))
        await state.finish()
    elif message.text in dates:
        zodiac_sign = data.get('zodiac_sign')
        horoscope = horoscope_all.get(message.text).get(zodiac_sign)

        await message.answer(text=f'<b>{zodiac_sign}</b> - гороскоп {message.text.lower()}:'
                                  f'\n{horoscope}', reply_markup=ReplyKeyboardRemove())
        await asyncio.sleep(1)
        await state.finish()
        await message.answer('Что-нибудь ещё?', reply_markup=determine_keyboad(message.from_user.id))
    else:
        await message.answer(text='Вы ввели несуществующий отрезок времени. Попробуйте ещё раз.')


def register(dp: Dispatcher):
    dp.register_message_handler(callback=return_zodiacs_keyboard, text='Посмотреть гороскоп по всем знакам зодиака')
    dp.register_message_handler(callback=return_date_keyboard, state=ShowHoroscope.zodiac_choice)
    dp.register_message_handler(callback=return_horoscope, state=ShowHoroscope.date_choice)
