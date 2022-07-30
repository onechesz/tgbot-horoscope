from aiogram.types import Message
from aiogram import Dispatcher


async def user_command_start_handler(message: Message):
    await message.answer(text='Здравствуйте, чего бы Вы хотели?', reply_markup=)


def register(dp: Dispatcher):
    dp.register_message_handler(callback=user_command_start_handler, commands=['start'])
