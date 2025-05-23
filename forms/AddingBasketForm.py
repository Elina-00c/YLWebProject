from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddingBasketForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    price = StringField('Цена', validators=[DataRequired()])
    provider = StringField('Поставщик', validators=[DataRequired()])
    number = StringField('Кол-во', validators=[DataRequired()])
    submit = SubmitField('Добавить')