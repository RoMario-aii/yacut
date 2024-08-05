import re
from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id
from .constants import SHORT_LENGTH, FORM_VALIDATORS, SERVER_URL


@app.route('/api/id/', methods=['POST'])
def get_short_url():
    if not request.data:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    data = request.get_json()

    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    elif 'custom_id' not in data or (
        data['custom_id'] == '' or data['custom_id'] is None
    ):
        data['custom_id'] = get_unique_short_id()
    else:
        short_link = data['custom_id']
        if len(short_link) > SHORT_LENGTH or (
            re.match(FORM_VALIDATORS, short_link) is None
        ):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )
        if URLMap.query.filter_by(short=short_link).first() is not None:
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.'
            )

    url_in_db = URLMap()
    url_in_db.from_dict(data)
    db.session.add(url_in_db)
    db.session.commit()

    return jsonify({
        'url': url_in_db.to_dict()['original'],
        'short_link': SERVER_URL + url_in_db.to_dict()['short']
    }), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_opinion(short_id):
    print(short_id)
    url_in_db = URLMap.query.filter_by(short=short_id).first()
    if url_in_db is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({
        'url': url_in_db.to_dict()['original'],
    }), HTTPStatus.OK
