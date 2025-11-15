from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField, StringField
from wtforms.validators import DataRequired


class ShoppingForm(FlaskForm):
    title = None
    product = StringField('Product name', validators=[DataRequired()])
    brand = StringField('Brand name', validators=[DataRequired()])
    color = StringField('Color name', validators=[DataRequired()])
    submit = SubmitField('Submit')





