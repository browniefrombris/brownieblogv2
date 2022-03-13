from ctypes import resize
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    post = TextAreaField('Say something:', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')
