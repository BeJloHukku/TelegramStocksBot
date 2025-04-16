from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command
from .utils import get_stock_price, get_price_for_russian_stock



router = Router()

@router.message(Command('quote'))
async def cmd_quote(message:types.Message):
    await message.answer("Введите тикер акции, например: AAPL")



# async def process_ticker(message: types.Message, state: FSMContext):
#     ticker = message.text.upper()
#     try:
#         try:
#             price = get_stock_price(ticker)  
#             await message.answer(
#                 f"📊 Котировка {ticker}: {price:.2f} USD\n"
#                 "Чтобы узнать другие котировки, введите /quote"
#             )
#         except Exception as e:
#             price = get_price_for_russian_stock(ticker)  
#             await message.answer(
#                 f"📊 Котировка {ticker}: {price:.2f} RUB\n"
#                 "Чтобы узнать другие котировки, введите /quote"
#             )
            
#     except Exception as e:
#         await message.answer(
#             "❌ Не удалось получить данные по этому тикеру.\n"
#             "Проверьте правильность написания (например: AAPL, SBER).\n"
#             "Для российских акций используйте тикеры без .ME"
#         )
    
#     await state.clear()



@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer('Привет! Я бот для мониторинга ценных бумаг. Используй /quote для получения котировки.')