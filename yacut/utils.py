import random

from .constants import SYMBOLS_CHOICE


def get_unique_short_id():
    short = random.choices(SYMBOLS_CHOICE, k=6)
    return ''.join(short)
