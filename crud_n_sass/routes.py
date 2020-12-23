from __init__ import app, db
from flask import render_template, request, json, jsonify, Response, url_for, session, redirect


@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html", login=False)
