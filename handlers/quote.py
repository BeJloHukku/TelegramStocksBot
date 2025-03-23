from aiogram import types, F
from utils import get_stock_price
from aiogram.fsm.context import FSMContext
from states import Form
import logging

logger = logging.getLogger(__name__)

async def cmd_quote(message:types.Message, state: FSMContext):
    logger.info(f"Пользователь {message.from_user.id} запросил котировку")
    await message.answer("Введите тикер акции, например: AAPL")
    await state.set_state(Form.waiting_for_ticket)


async def process_ticker(message: types.Message, state:FSMContext):
    ticker = message.text.upper()
    logger.info(f"Пользователь {message.from_user.id} ввел тикер: {ticker}")
    try:
        price = get_stock_price(ticker)
        await message.answer(
            f'''Котировка {ticker}: {price:.2f} USD
Чтобы узнать другие котировки введите /quote''')
    except Exception as e:
        logger.error(f"Ошибка при обработке команды /quote: {e}", exc_info=True)  
        await message.answer(f"Не знаю такого тикера(")
    await state.clear()

