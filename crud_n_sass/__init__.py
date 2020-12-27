from flask import Flask, render_template
from sassutils.wsgi import SassMiddleware
from crud_n_sass.config import Config
from flask_mongoengine import MongoEngine


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev"
    )
    app.config.from_object(Config)
    app.wsgi_app = SassMiddleware(app.wsgi_app, {
        'crud_n_sass': ('static/sass', 'static/css', '/static/css')
    })

    db = MongoEngine()
    db.init_app(app)

    from crud_n_sass import todo
    app.register_blueprint(todo.bp)

    app.add_url_rule("/", endpoint="index")

    return app
