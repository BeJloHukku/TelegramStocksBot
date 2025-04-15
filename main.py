import asyncio
import config as cfg
from app.handlers import router
from aiogram import Bot, Dispatcher






bot = Bot(token=cfg.BOT_TOKEN)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    dp.include_router(router)
    asyncio.run(main())