from apscheduler.schedulers.asyncio import AsyncIOScheduler

from core.data.__init__ import db
from core.parsers.horoscope import get_content as get_horoscope


async def update_horoscope():
    horoscope_daily = get_horoscope(url='https://74.ru/horoscope/daily/')

    for zodiac_sign in horoscope_daily:
        db.update_horoscope(zodiac_sign=zodiac_sign, horoscope=horoscope_daily.get(zodiac_sign))


def register(scheduler: AsyncIOScheduler):
    scheduler.add_job(func=update_horoscope, trigger='cron', hour=8, minute=50)
