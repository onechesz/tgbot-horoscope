from dataclasses import dataclass
from environs import Env


@dataclass
class DBConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TGBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tgbot: TGBot
    db: DBConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tgbot=TGBot(
            token=env.str('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMINS'))),
            use_redis=env.bool('USE_REDIS')
        ),
        db=DBConfig(
            host=env.str('PGHOST'),
            password=env.str('PGPASSWORD'),
            user=env.str('PGUSER'),
            database=env.str('PGNAME')
        ),
        misc=Miscellaneous()
    )
