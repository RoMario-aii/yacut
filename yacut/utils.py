import string
from random import choice

from settings import UNIQUE_ID_LENGTH

from .models import URLMap


def get_unique_short_id(chars=string.ascii_letters + string.digits):
    short_id = ''.join([choice(chars) for i in range(UNIQUE_ID_LENGTH)])
    if URLMap.query.filter_by(short=short_id).first():
        short_id = get_unique_short_id()
    return short_id
