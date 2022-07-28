from aiogram import Dispatcher
from aiogram.types import Message

from core.data.__init__ import db
from core.parsers.horoscope import horoscope as horoscope_all


async def personal_horoscope(message: Message):
    if not db.select_user_zodiac_sign(user_id=message.from_user.id)[0]:
        await message.answer(text='Вы не можете узнать личный гороскоп, поскольку ещё не указали свой знак зодиака')
    else:
        date = message.text[9:].capitalize()
        zodiac_sign = db.select_user_zodiac_sign(user_id=message.from_user.id)[0]
        horoscope = horoscope_all.get(date).get(zodiac_sign)

        await message.answer(text=f'<b>{zodiac_sign}</b> - гороскоп {date.lower()}:'
                                  f'\n{horoscope}')


def register(dp: Dispatcher):
    dp.register_message_handler(callback=personal_horoscope, text=['Гороскоп на сегодня', 'Гороскоп на завтра',
                                                                   'Гороскоп на неделю'])
