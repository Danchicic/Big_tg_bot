import asyncio
from aiogram import Bot, Dispatcher
from config.config import import_config, Config
from handlers.Reader import Reader_router
from handlers.default_user_handlers import user_router
from keyboards.menu import set_main_menu

config: Config = import_config('.env')


# ToDo: Сделать /start

async def main() -> None:
    bot: Bot = Bot(token=config.TgBot.token)
    dp: Dispatcher = Dispatcher()

    await set_main_menu(bot)

    dp.include_router(user_router)

    dp.include_router(Reader_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
