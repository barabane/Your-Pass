import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from handlers import create_password

load_dotenv()

bot = Bot(os.environ.get('BOT_KEY'))
dp = Dispatcher(bot)


dp.register_message_handler(create_password, regexp='[1234567890]')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
