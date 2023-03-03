from loguru import logger
from aiogram.types import Message, KeyboardButton
from src.utils import generate_password, kb
from src.database.db import db
from src.fsm import UserState


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
    await msg.answer(f"Длинна: {settings['length']} /length \nЦифры: {'вкл' if settings['numbers'] else 'выкл'} /numbers \nСпец. символы: {'вкл' if settings['symbols'] else 'выкл'} /symbols", parse_mode='HTML')


async def change_settings_handler(msg: Message):
    user_settings = db.get_settings(user_id=msg.from_user.id)

    command = msg.get_command()[1:]

    if command == 'length':
        await msg.answer('Укажите новую длинну пароля:')
        await UserState.change_pass_length.set()
        return
    else:
        user_settings[command] = not user_settings[command]

    db.change_settings(user_id=msg.from_user.id,
                       new_settings=f"{user_settings}")

    await msg.answer('Настройки изменены')
    await msg.answer(f"Длинна: {user_settings['length']} /length \nЦифры: {'вкл' if user_settings['numbers'] else 'выкл'} /numbers \nСпец. символы: {'вкл' if user_settings['symbols'] else 'выкл'} /symbols", parse_mode='HTML')


async def change_pass_length_handler(msg: Message):
    settings = db.get_settings(msg.from_user.id)
    settings['length'] = int(msg.text)

    db.change_settings(msg.from_user.id, f'{settings}')
    await msg.answer('Настройки изменены')
    await UserState.previous()
    await msg.answer(f"Длинна: {settings['length']} /length \nЦифры: {'вкл' if settings['numbers'] else 'выкл'} /numbers \nСпец. символы: {'вкл' if settings['symbols'] else 'выкл'} /symbols", parse_mode='HTML')


async def generate_password_handler(msg: Message):
    settings = db.get_settings(msg.from_user.id)

    password = generate_password(
        length=settings['length'], symbols_on=settings['symbols'], numbers_on=settings['numbers'])
    await msg.answer(password)
