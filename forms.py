from turtle import title
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Tytul', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    year = FloatField('Rok', validators=[DataRequired()])

