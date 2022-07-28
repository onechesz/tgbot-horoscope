import sqlite3

from aiogram import Dispatcher
from aiogram.types import Message

from core.data.__init__ import db
from core.handlers.determine_start_keyboard import determine_keyboad


async def start(message: Message):
    if db.count_user(user_id=message.from_user.id)[0] == 0:
        db.add_user(user_id=message.from_user.id)

    await message.answer('Здравствуйте. Чего бы Вы хотели?', reply_markup=determine_keyboad(message.from_user.id))


def register(dp: Dispatcher):
    dp.register_message_handler(callback=start, commands=['start'])
