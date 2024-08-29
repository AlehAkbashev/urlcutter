from flask import render_template, request

from ya_cut import app, db
from .forms import CutForm
from .models import URLMap

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def add_url():
    form = CutForm()
    if form.validate_on_submit():
        short_url = URLMap(
            short=form.data['short'],
            original=form.data['original']
        )
        db.session.add(short_url)
        db.session.commit()