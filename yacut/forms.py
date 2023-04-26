from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp


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
            Length(1, 16),
            Optional(),
            Regexp(
                r"^[a-zA-Z0-9]{1,6}$",
                message="Должна строка длиной от 1 до 6 символов и содержащая только латинские буквы или цифры",
            ),
        ],
    )
    submit = SubmitField("Создать")
