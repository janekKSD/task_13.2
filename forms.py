from turtle import title
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    #id = FloatField('id', validators=[DataRequired()])
    title = StringField('Tytul', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    year = FloatField('Rok', validators=[DataRequired()])
