import os
from loguru import logger
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from src.handlers import start_handler, generate_password_handler, change_settings_handler, settings_handler, change_pass_length_handler
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from src.fsm import UserState

storage = MemoryStorage()
load_dotenv()

bot = Bot(os.environ.get('BOT_KEY'))
dp = Dispatcher(bot, storage=storage)


dp.register_message_handler(start_handler, commands=['start', 'help'])
dp.register_message_handler(
    generate_password_handler, lambda msg: msg.text == '👁‍🗨 Сгенерировать пароль')
dp.register_message_handler(
    settings_handler, lambda msg: msg.text == '⚙️ Настройки')
dp.register_message_handler(
    change_settings_handler, commands=['length', 'numbers', 'symbols'])
dp.register_message_handler(
    change_pass_length_handler, regexp='[0123456789]', state=UserState.change_pass_length)

if __name__ == "__main__":
    logger.info("bot's working...")
    executor.start_polling(dp, skip_updates=True)
