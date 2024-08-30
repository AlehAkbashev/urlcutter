import random

from yacut import app
from .models import URLMap


def get_unique_short_id():
    alphabet = app.config['ALPHABET']
    result = ''.join([random.choice(alphabet) for i in range(app.config['URL_LEN'])])
    while URLMap.query.filter_by(short=result).first():
        result = ''.join([random.choice(alphabet) for i in range(app.config['URL_LEN'])])
    return result

