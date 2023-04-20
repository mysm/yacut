from flask import abort, flash, redirect, render_template, url_for

from . import app


@app.route("/")
def index_view():
    return render_template("index.html")
