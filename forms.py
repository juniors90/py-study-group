"""

PROJECT: "Imagine a Github Profile Finder"

AUTHOR: juniors

CREATED AT: 22/02/2021

"""

from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField
from wtforms.fields.core import StringField
from wtforms.validators import DataRequired, Length

class SearchProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    submit = SubmitField('Search User')