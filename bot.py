import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Config and DB:
from core.config import load_config
from core.utils.db_api.postgresql import Database

# Middlewares:
# ---

# Filters:
# ---

# Handlers:
from core.handlers.user_command_start import register as user_command_start

# Schedulers:
# ---

logger = logging.getLogger(__name__)


def register_middlewares(dp: Dispatcher, config):
    pass


def register_filters(dp: Dispatcher):
    pass


def register_handlers(dp: Dispatcher):
    user_command_start(dp=dp)


def schedulers(scheduler: AsyncIOScheduler, bot: Bot, db: Database):
    pass


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
    db = Database(loop=dp.loop)
    scheduler = AsyncIOScheduler()
    bot['config'] = config

    register_middlewares(dp=dp, config=config)
    register_filters(dp=dp)
    register_handlers(dp=dp)
    schedulers(scheduler=scheduler, bot=bot, db=db)

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
