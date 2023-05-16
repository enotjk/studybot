from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



from config import TOKEN_API, HELP_COMMAND, kb

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text="Добро пожаловать в наш бот!",
                           parse_mode="HTML",
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text="наш бот умеет отправлять фотографии",
                           parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://lifeglobe.net/x/entry/1032/Smile.JPG')
    await message.delete()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)