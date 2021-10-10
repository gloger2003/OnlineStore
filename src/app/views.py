from flask.templating import render_template_string
from app import (app, db)


@app.route('/')
@app.route('/index/')
def index():
    return '<h1>Привет!</h1>'