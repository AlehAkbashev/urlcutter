import re

from flask import request, jsonify

from yacut import app, db
from .error_handlers import APIUsageError
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/api/id/', methods=["POST"])
def create_id():
    data = request.get_json()
    if 'url' not in data:
        raise APIUsageError('"url" является обязательным полем!')
    else:
        if re.match(r'^https*:\/\/[a-z0-9]+.', data['url']) is None:
            raise APIUsageError('Your url is not url')
    if 'custom_id' in data and data['custom_id'] != '':
        if URLMap.query.filter_by(short=data['custom_id']).first():
            raise APIUsageError('Предложенный вариант короткой ссылки уже существует.')
        elif re.match(app.config['USER_PATTERN'], data['custom_id']) is None:
            raise APIUsageError('Указано недопустимое имя для короткой ссылки')
        else:
            custom_id = data['custom_id']
    else:
        custom_id = get_unique_short_id()
    short_url = URLMap(
        original=data['url'],
        short=custom_id
    )
    db.session.add(short_url)
    db.session.commit()
    return jsonify(short_url.to_dict()), 201