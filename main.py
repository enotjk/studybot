from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN_API


HELP_COMMAND = """
/help - список команд
/start - начать роботу с ботом
/description - описание бота
"""
DESCRIPTION_BOT = """
Я бот созданый для тестирование и обучению создание ботов
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(text="Привет, я Бот!")
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.reply(text=DESCRIPTION_BOT)

if __name__ == '__main__':
    executor.start_polling(dp)