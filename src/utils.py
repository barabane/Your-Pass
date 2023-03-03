import random
import string
from loguru import logger
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def kb(buttons: [KeyboardButton]):
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def generate_password(length: int, symbols_on, numbers_on):
    password = ''

    while len(password) < length:
        password += random.choice(string.ascii_letters)

        if symbols_on:
            password += random.choice(string.punctuation)
        if numbers_on:
            password += random.choice(string.digits)

    return password[:length]
