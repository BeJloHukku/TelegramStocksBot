from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from .utils import get_information, safe_json_parse
import app.keyboards as kb
from .states import AddingState

from .database import request as rq

router = Router()



@router.message(CommandStart())
async def cmd_start(message : Message):
    await rq.set_user(message.from_user.id, message.from_user.first_name)
    await message.answer(f'Привет, {message.from_user.first_name}! Я бот для мониторинга ценных бумаг.', reply_markup=kb.to_main)


@router.message(Command('quote'))
async def cmd_quote(message : Message):
    await message.answer("Введите тикер акции, например: SBER")


@router.callback_query(F.data == 'main_menu')
async def main_menu(callback : CallbackQuery, state : FSMContext):
    await callback.answer('Вы перешли в главное меню!')
    await state.clear()
    await callback.message.answer('Привет! Это главное меню!', reply_markup=kb.main_menu)


@router.callback_query(F.data == 'help')
async def help(callback : CallbackQuery):
    await callback.answer('Вы перешли в раздел "Помощь"')
    await callback.message.answer('Это раздел помощь!', reply_markup=kb.to_main)


@router.callback_query(F.data == 'bag')
async def bag(callback : CallbackQuery):
    await callback.answer('Вы перешли в раздел "Портфель"')

    bag = await rq.open_bag(callback.from_user.id)
    tickers = safe_json_parse(bag if bag else None, default=[])

    if bag == None:
        await callback.message.edit_text('К сожалению, вы еще не зарегистрированы. ' \
                                        'Для регистрации запустите команду /start', reply_markup=kb.to_main)
    elif bag == []:
        await callback.message.edit_text('Ваш портфель пуст!', reply_markup=kb.to_main)
    else:
        message = "📊 Ваш портфель:\n" + "\n".join(
            f"• {ticker}" for ticker in tickers
        )
        await callback.message.edit_text(message, reply_markup= await kb.inline_stocks(tickers))


@router.callback_query(F.data == 'price')
async def check_price(callback : CallbackQuery, state : FSMContext):
    await callback.answer('')
    await state.set_state(AddingState.stock)
    await callback.message.edit_text("Введите тикер акции!")


@router.message(AddingState.stock)
async def show_price(message : Message, state : FSMContext):
    stock = message.text
    await state.update_data(stock=stock)
    try:
        await message.answer(
            f"📊 Акция {stock.upper()}\n"
            f"💰 Текущая цена: {get_information(stock.upper())['LAST']}\n\n"
            "📝 Введите другой тикер или добавьте эту акцию в портфель",
            reply_markup=kb.after_checking_price,
        )
    except Exception as e:
        await state.update_data(stock=None)
        await message.answer(
            "🔍 Тикер не найден.\n"
            "Попробуйте ввести другой тикер, например: SBER, GAZP"
        )


@router.callback_query(F.data == 'add')
async def add_to_bag(callback : CallbackQuery, state : FSMContext):
    await callback.answer('Добавление акции...')
    stock = await state.get_data()
    success = await rq.add_stock(callback.from_user.id, stock['stock'])
    if success:
        await callback.message.answer("Акция успешно добавлена")
    else:
        await callback.message.answer("Ошибка добавления акции")
        await state.update_data(stock=None)


@router.callback_query(F.data.startswith('stock_'))
async def show_stock_info(callback : CallbackQuery):
    await callback.answer('Echo')
    ticker = callback.data.split('_')[1]
    info = get_information(ticker)
    await callback.message.edit_text(f"Название: {info['shortname']}\n \
                                     Цена: {info['LAST']} \n ")
