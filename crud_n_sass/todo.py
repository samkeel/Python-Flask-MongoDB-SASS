from flask import Blueprint, render_template, redirect, request, url_for

bp = Blueprint("todo", __name__)


@bp.route("/")
def index():
    return render_template("todo/index.html")