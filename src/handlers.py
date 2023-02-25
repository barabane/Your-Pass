from aiogram.types import Message, KeyboardButton
from src.utils import generate_password, kb


async def start_handler(msg: Message):
    keybr = kb(buttons=[
        [KeyboardButton('👁‍🗨 Сгенерировать пароль')],
        # [KeyboardButton('⚙️ Профиль')]
    ])
    await msg.answer('Меню', reply_markup=keybr)


async def generate_password_handler(msg: Message):
    await msg.answer('Введите желаемую длинну пароля:')


async def create_password_handler(msg: Message):
    if int(msg.text) > 20:
        await msg.answer('Пароль должен быть не длинне 20 символов !')
        return
    elif int(msg.text) < 3:
        await msg.answer('Пароль должен быть не короче 3 символов !')
        return

    await msg.answer(f'```{generate_password(int(msg.text))}```', parse_mode='Markdown')
