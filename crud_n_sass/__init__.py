from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from sassutils.wsgi import SassMiddleware
from crud_n_sass.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'crud_n_sass': ('static/sass', 'static/css', '/static/css')
})


db = MongoEngine()
db.init_app(app)


@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html", login=False)


if __name__ == '__main__':
    app.run(debug=True)
