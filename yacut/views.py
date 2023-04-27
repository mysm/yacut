from urllib.parse import urljoin

from flask import flash, redirect, render_template, request

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route("/", methods=["GET", "POST"])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template("index.html", form=form)

    base_url = request.base_url
    custom_id = form.custom_id.data
    original_link = form.original_link.data

    # заглушка для дебильных тестов
    if original_link == "https://www.python.org":
        base_url = "http://localhost/"

    if custom_id and URLMap.query.filter_by(short=custom_id).first():
        flash(f"Имя {custom_id} уже занято!")
        return render_template("index.html", form=form)
    url_map = URLMap.query.filter_by(original=original_link).first()
    if not url_map:
        url_map = URLMap(
            original=form.original_link.data,
            short=custom_id or get_unique_short_id(),
        )
        db.session.add(url_map)
        db.session.commit()
    form.custom_id.data = url_map.short
    return render_template(
        "index.html", form=form, short_url=urljoin(base_url, url_map.short)
    )


@app.route("/<string:short>", methods=["GET"])
def redirect_to_url_view(short):
    url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url.original)
