import logging
import asyncio
import config as cfg
from handlers import cmd_start, cmd_quote, process_ticker
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from states import Form

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Формат сообщений
    filename="bot.log",  # Логи будут записываться в файл bot.log
)

logger = logging.getLogger(__name__)

# Вставьте сюда ваш токен
API_TOKEN = cfg.BOT_TOKEN
# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


dp.message.register(cmd_start, Command("start"))
dp.message.register(cmd_quote, Command("quote"))
dp.message.register(
    process_ticker,
    Form.waiting_for_ticket,
    F.text
)

# Запуск бота
async def main():
    logger.info("Бот запущен")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())