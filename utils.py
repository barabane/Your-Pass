import random

numbers = '1234567890'
letters = 'qwertyuiopasdfghjklzxcvbnm'
symbols = '!@#$%^&*)(_-+=}{><?'


def generate_part(length=1):
    part = ''

    arr = random.choices(numbers+letters+symbols, k=length)
    for sign in arr:
        part += sign

    return part


def generate_password(length=3):
    password = ''
    cycles = length // 3

    for _ in range(cycles):
        password += generate_part(3)

    if length % 3:
        password += generate_part(length % 3)

    return password
