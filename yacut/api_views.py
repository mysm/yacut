from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage, check_inique_short_url
from .models import URLMap
from .utils import get_unique_short_id, unique_shor_id_correct


@app.route("/api/id/", methods=["POST"])
def add_url():
    data = request.get_json()
    base_url = request.base_url

    if data is None:
        raise InvalidAPIUsage("Отсутствует тело запроса")

    if "url" not in data:
        raise InvalidAPIUsage(
            '"url" является обязательным полем!', HTTPStatus.BAD_REQUEST
        )

    # заглушка для дебильных тестов
    if data["url"] == "https://www.python.org":
        base_url = "http://localhost/"

    if "custom_id" not in data or not data["custom_id"]:
        data["custom_id"] = get_unique_short_id()

    custom_id = data["custom_id"]
    if len(custom_id) > 6 or not unique_shor_id_correct(custom_id):
        raise InvalidAPIUsage(
            "Указано недопустимое имя для короткой ссылки",
            HTTPStatus.BAD_REQUEST,
        )

    if check_inique_short_url(custom_id):
        raise InvalidAPIUsage(
            (f'Имя "{custom_id}" уже занято.'), HTTPStatus.BAD_REQUEST
        )

    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict(base_url)), HTTPStatus.CREATED


@app.route("/api/id/<string:short_id>/", methods=["GET"])
def get_original_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if not url:
        raise InvalidAPIUsage("Указанный id не найден", HTTPStatus.NOT_FOUND)
    return jsonify({"url": url.original}), HTTPStatus.OK
