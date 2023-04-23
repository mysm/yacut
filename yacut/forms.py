from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    original_link = URLField(
        "Ссылка",
        validators=[DataRequired(message="Обязательное поле"), Length(1, 256)],
    )
    custom_id = URLField(
        "Ваш вариант короткой ссылки",
        validators=[Length(1, 256), Optional()],
    )
    submit = SubmitField("Создать")
