from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from core.data.__init__ import db


async def horoscope_notify(bot: Bot = None):
    user_ids = db.select_all_user_ids()

    for i in range(len(user_ids)):
        user_ids[i] = tuple((user_ids[i][0],
                             db.select_horoscope_by_sign(db.select_user_zodiac_sign(user_ids[i][0])[0])[0]))

    for t in user_ids:
        await bot.send_message(chat_id=t[0], text=f'<b>Доброе утро. Ваш гороскоп на сегодня:</b>\n{t[1]}')


def register(scheduler: AsyncIOScheduler, bot: Bot):
    scheduler.add_job(horoscope_notify, 'cron', [bot], hour=9, minute=00)
