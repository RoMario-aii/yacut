from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .constants import FORM_VALIDATORS


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[Length(1, 256),
                    DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Optional(),
            Regexp(FORM_VALIDATORS, message='Введены недопустимые символы')
        ]
    )
    submit = SubmitField('Создать')