import asyncio

import asyncpg

from core.config import load_config

config = load_config('../../.env')


class Database:

    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = loop.run_until_complete(asyncpg.create_pool(
            user=config.db.user,
            password=config.db.password,
            host=config.db.host,
            port=5432,
            database=config.db.database
        ))

    async def add_user(self):
        sql = '''
        
        '''
