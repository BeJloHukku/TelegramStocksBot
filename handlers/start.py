from aiogram import types
import logging

logger = logging.getLogger(__name__)

async def cmd_start(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} запустил бота")
    await message.answer('Привет! Я бот для мониторинга ценных бумаг. Используй /quote для получения котировки.')
    