import re

from string import ascii_letters, digits

UNIQUE_ID_LENGTH = 6
FORM_VALIDATORS = re.compile(r'^[a-zA-Z0-9]{1,16}$')
SHORT_LENGTH = 16
SERVER_URL = 'http://localhost/'
SYMBOLS_CHOICE = list(ascii_letters + digits)
