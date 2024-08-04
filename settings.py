import os
import re


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', default='SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


UNIQUE_ID_LENGTH = 6
FORM_VALIDATORS = re.compile(r'^[a-zA-Z0-9]{1,16}$')
