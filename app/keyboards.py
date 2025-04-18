from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup,  KeyboardButton, InlineKeyboardButton
from .utils import text

to_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=text.get('buttons', 'main'), callback_data='main_menu')]
])


main_menu = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text=text.get('buttons', 'price'), callback_data='price')], 
    [InlineKeyboardButton(text=text.get('buttons', 'bag'), callback_data='bag')], 
    [InlineKeyboardButton(text=text.get('buttons', 'help'), callback_data='help')]
],)