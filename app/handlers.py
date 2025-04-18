from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from .utils import get_information, safe_json_parse
import app.keyboards as kb

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
async def main_menu(callback : CallbackQuery):
    await callback.answer('Вы перешли в главное меню!')
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
        await callback.message.answer('К сожалению, вы еще не зарегистрированы. ' \
                                        'Для регистрации запустите команду /start', reply_markup=kb.to_main)
    elif bag == []:
        await callback.message.answer('Ваш портфель пуст!', reply_markup=kb.to_main)
    else:
        message = "📊 Ваш портфель:\n" + "\n".join(
            f"• {ticker}" for ticker in tickers
        )
        await callback.message.answer(message)