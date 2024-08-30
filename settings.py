import os
import string


class Settings(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")

    PREFIX_URL = 'http://localhost:5000/'
    USER_PATTERN = r'^[a-zA-Z0-9]{1,16}$'
    URL_LEN = 6
    ALPHABET = string.ascii_lowercase + string.ascii_uppercase + string.digits
