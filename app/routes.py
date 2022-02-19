from app import app
from flask import render_template, send_from_directory
import os

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'B_logo.ico', mimetype = 'image/png')


@app.route('/recipes')
def recipes():
    return render_template('recipes.html')