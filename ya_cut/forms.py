from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import URL, DataRequired, Length


class CutForm(FlaskForm):
    original = URLField(validators=[DataRequired(),])
    short = URLField(validators=[URL(), Length(16)])
    submit = SubmitField('Создать')