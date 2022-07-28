from typing import Optional
from aiogram.dispatcher.filters import BoundFilter

from core.config import Config


class Admin(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, obj) -> bool:
        if self.is_admin is None:
            return False

        config: Config = obj.bot.get('config')

        return (obj.from_user.id in config.tgbot.admin_ids) == self.is_admin
