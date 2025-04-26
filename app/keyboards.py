from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup,  KeyboardButton, InlineKeyboardButton
from .utils import text
from aiogram.utils.keyboard import InlineKeyboardBuilder

button_to_main = InlineKeyboardButton(text=text.get('buttons', 'main'), callback_data='main_menu')

to_main = InlineKeyboardMarkup(inline_keyboard=[
    [button_to_main]
])


main_menu = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text=text.get('buttons', 'price'), callback_data='price')], 
    [InlineKeyboardButton(text=text.get('buttons', 'bag'), callback_data='bag')], 
    [InlineKeyboardButton(text=text.get('buttons', 'help'), callback_data='help')]
])


after_checking_price = InlineKeyboardMarkup(inline_keyboard=[
    [button_to_main, InlineKeyboardButton(text=text.get('buttons', 'add_stock'), callback_data='add')]
])


async def inline_stocks(stocks: list):
    keyboard = InlineKeyboardBuilder()
    for stock in stocks:
        keyboard.add(InlineKeyboardButton(text=stock, callback_data=f'stock_{stock}'))
    return keyboard.adjust(2).as_markup()