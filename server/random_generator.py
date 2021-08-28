from random import choice
from random import randint
from string import digits
from string import ascii_letters

INTEGER_DIGIT = 12
STRING_LENGTH = 16


def generate_id() -> int:
    return randint(0, (10 ** INTEGER_DIGIT) - 1)


def generate_string() -> str:
    return ''.join(
        choice(digits + ascii_letters)
        for i in range(STRING_LENGTH))
