from loguru import logger
from aiogram.types import Message, KeyboardButton
from src.utils import generate_password, kb
from src.database.db import db


async def start_handler(msg: Message):
    db.reg_user(msg)
    keybr = kb(buttons=[
        [KeyboardButton("👁‍🗨 Сгенерировать пароль")],
        [KeyboardButton("⚙️ Настройки")]
    ])
    await msg.answer('Меню', reply_markup=keybr)


async def settings_handler(msg: Message):
    settings = db.get_settings(user_id=msg.from_user.id)
    logger.info(settings)
    await msg.answer(f"Длинна: {settings['length']} /length \nЦифры: {settings['numbers']} /numbers \nСпец. символы: {settings['symbols']} /symbols", parse_mode='HTML')


async def change_settings_handler(msg: Message):
    user_settings = db.get_settings(user_id=msg.from_user.id)

    command = msg.get_command()[1:]

    if command == 'length':
        await msg.answer('Укажите новую длинну пароля:')
        return
    else:
        user_settings[command] = not user_settings[command]

    db.change_settings(user_id=msg.from_user.id,
                       new_settings=f"{user_settings}")

    await msg.answer('Настройки изменены')
    await msg.answer(f"Длинна: {user_settings['length']} /length \nЦифры: {user_settings['numbers']} /numbers \nСпец. символы: {user_settings['symbols']} /symbols", parse_mode='HTML')


async def generate_password_handler(msg: Message):
    settings = db.get_settings(msg.from_user.id)
    password = generate_password(settings)
    await msg.answer(password)


async def create_password_handler(msg: Message):
    if int(msg.text) > 20:
        await msg.answer('Пароль должен быть не длинне 20 символов !')
        return
    elif int(msg.text) < 3:
        await msg.answer('Пароль должен быть не короче 3 символов !')
        return

    await msg.answer(f'```{generate_password(int(msg.text))}```', parse_mode='Markdown')
