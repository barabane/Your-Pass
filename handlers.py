from aiogram.types import Message
from utils import generate_password


async def create_password(msg: Message):
    if int(msg.text) > 20:
        await msg.answer('Пароль должен быть не длинне 20 символов !')
        return
    elif int(msg.text) < 3:
        await msg.answer('Пароль должен быть не короче 3 символов !')
        return

    await msg.answer(f'{generate_password(int(msg.text))}', parse_mode='HTML')
