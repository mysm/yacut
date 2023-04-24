from flask import abort, flash, redirect, render_template, url_for

from . import app
from .forms import URLMapForm
from .models import URLMap
from .generate_short_link import get_unique_short_id


@app.route("/", methods=["GET", "POST"])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
    return render_template("index.html", form=form)
