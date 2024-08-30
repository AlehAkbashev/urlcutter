from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, Optional, URL


class CutForm(FlaskForm):
    original_link = URLField(validators=[DataRequired(), URL()])
    custom_id = StringField(validators=[Length(1, 16), Optional()])
    submit = SubmitField('Создать')