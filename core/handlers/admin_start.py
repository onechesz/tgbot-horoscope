from aiogram import Dispatcher
from aiogram.types import Message


async def start(message: Message):
    await message.answer('Привет, администратор.')


def register(dp: Dispatcher):
    dp.register_message_handler(callback=start, commands=['start'], is_admin=True)
