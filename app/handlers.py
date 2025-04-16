from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command
from .utils import get_price

import app.database.requests as rq

router = Router()

@router.message(Command('quote'))
async def cmd_quote(message:types.Message):
    await message.answer("Введите тикер акции, например: AAPL")


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await rq.set_user(message.from_user.id, message.from_user.first_name)
    await message.answer(f'Привет, {message.from_user.first_name}! Я бот для мониторинга ценных бумаг. ')