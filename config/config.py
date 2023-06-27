from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    db_host: str


@dataclass
class Config:
    TgBot: TgBot


def import_config(path: str | None) -> Config:
    env = Env()
    env.read_env()
    return Config(
        TgBot=TgBot(
            token=env('BOT_TOKEN'),
            db_host=env('DB_HOST')
        )
    )
