from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


TOKEN_API = '6060675969:AAGYj0Pg7cI4olj6M_lQvAim6l2QrM3qNYo'
STIKER_ID = 'CAACAgIAAxkBAAEIzLVkTuQWYjpRmGzvD496EFOGanTNYAAC-hMAAgX-EUjymrnHnHf3BS8E'

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описани бота</em>
<b>/photo</b> - <em>отправка нашего фото</em>
"""


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/photo')
b3 = KeyboardButton('/description')
kb.add(b1).insert(b2).add(b3)
