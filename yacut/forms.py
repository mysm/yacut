from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL


class URLMapForm(FlaskForm):
    original_link = URLField(
        "Ссылка",
        validators=[
            DataRequired(message="Обязательное поле"),
            Length(1, 256),
            URL(message="введите корректный URL"),
        ],
    )
    custom_id = URLField(
        "Ваш вариант короткой ссылки",
        validators=[
            Length(1, 256),
            Optional(),
            URL(message="введите корректный URL"),
        ],
    )
    submit = SubmitField("Создать")
