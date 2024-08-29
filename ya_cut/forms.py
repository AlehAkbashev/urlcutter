from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, Optional


class CutForm(FlaskForm):
    original_link = URLField(validators=[DataRequired(),])
    custom_id = StringField(validators=[Length(1, 16), Optional()])
    submit = SubmitField('Создать')