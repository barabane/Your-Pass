import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from src.handlers import create_password_handler, start_handler, generate_password_handler

load_dotenv()

bot = Bot(os.environ.get('BOT_KEY'))
dp = Dispatcher(bot)


dp.register_message_handler(start_handler, commands=['start', 'help'])
dp.register_message_handler(
    generate_password_handler, lambda msg: msg.text == '👁‍🗨 Сгенерировать пароль')
dp.register_message_handler(create_password_handler, regexp='[1234567890]')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
