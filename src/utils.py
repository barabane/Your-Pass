import random
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

numbers = '1234567890'
letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
symbols = '!@#$%^&*)(_-+=}{><?'


def kb(buttons: [KeyboardButton]):
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


# def generate_part(length=1, symbols_on=True, numbers_on=True):
#     part = ''

#     arr = random.choices(numbers+letters+symbols, k=length)

#     for sign in arr:
#         part += sign

#     return part


def generate_password(settings):
    length = settings['length']
    symbols_on = settings['symbols']
    numbers_on = settings['numbers']

    password = ''

    for _ in range(length):
        if symbols_on and numbers_on:
            password += random.choice(letters+numbers+symbols)
        elif symbols and not numbers:
            password += random.choice(letters+symbols)
        elif numbers and not symbols:
            password += random.choice(letters+numbers)
        else:
            password += random.choice(letters)

    return password
