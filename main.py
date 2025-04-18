import asyncio
import config as cfg
from app import router
from aiogram import Bot, Dispatcher
from app import async_main




async def main():
    await async_main()
    bot = Bot(token=cfg.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())