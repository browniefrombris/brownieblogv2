from wtforms.fields.simple import SubmitField
from app import app, db
from app.forms import PostForm
from app.models import Post, User
from flask import render_template, send_from_directory, url_for, flash, redirect
import os

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()
    user = {'username': 'everyone'}
    
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=User.query.get(1))
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    
    posts = Post.query.all()
    
    return render_template('index.html', title='Home', user=user, form=form, posts=posts)

@app.route('/clear_database', methods=['GET', 'POST'])
def clear_database():
    Post.query.delete()
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'B_logo.ico', mimetype = 'image/png')


@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')