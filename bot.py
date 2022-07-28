import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from core.config import load_config
from core.filters.admin import Admin
from core.handlers.admin_start import register as admin_start
from core.handlers.user_start import register as user_start
from core.handlers.select_zodiac_sign import register as select_zodiac_sign
from core.handlers.show_horoscope import register as show_horoscope
from core.handlers.personal_horoscope import register as personal_horoscope
from core.data.horoscope import register as horoscope_scheduler
from core.schedules.horoscope import register as horoscope_notifier_scheduler

logger = logging.getLogger(__name__)


def register_middlewares(dp: Dispatcher, config):
    pass


def register_filters(dp: Dispatcher):
    dp.filters_factory.bind(Admin)


def register_handlers(dp: Dispatcher):
    # admin_start(dp=dp)
    user_start(dp=dp)
    select_zodiac_sign(dp=dp)
    show_horoscope(dp=dp)
    personal_horoscope(dp=dp)


def schedulers(scheduler: AsyncIOScheduler, bot: Bot):
    horoscope_scheduler(scheduler)
    horoscope_notifier_scheduler(scheduler, bot)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('Bot started.')

    config = load_config('.env')
    storage = RedisStorage2() if config.tgbot.use_redis else MemoryStorage()
    bot = Bot(token=config.tgbot.token, parse_mode='HTML')
    dp = Dispatcher(bot=bot, storage=storage)
    scheduler = AsyncIOScheduler()
    bot['config'] = config

    register_middlewares(dp=dp, config=config)
    register_filters(dp=dp)
    register_handlers(dp=dp)
    schedulers(scheduler=scheduler, bot=bot)
    #
    # try:
    #     db.create_table_horoscope()
    #     db.insert_zodiac_signs()
    # except Exception as err:
    #     print(err)
    #
    # try:
    #     db.create_table_users()
    # except Exception as err:
    #     print(err)

    try:
        scheduler.start()
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped.')
