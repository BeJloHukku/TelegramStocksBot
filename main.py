import logging
import asyncio
import config as cfg
from handlers import cmd_start, cmd_quote, process_ticker
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from states import Form

#Логирование
logging.basicConfig(
    level=logging.INFO,  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  
    filename="bot.log", 
)
logger = logging.getLogger(__name__)


bot = Bot(token=cfg.BOT_TOKEN)
dp = Dispatcher()

#Регистрация обработчиков
dp.message.register(cmd_start, Command("start"))
dp.message.register(cmd_quote, Command("quote"))
dp.message.register(
    process_ticker,
    Form.waiting_for_ticket,
    F.text
)

#Запуск бота
async def main():
    logger.info("Бот запущен")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())