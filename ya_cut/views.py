from flask import render_template, request, redirect

from ya_cut import app, db
from .forms import CutForm
from .models import URLMap

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CutForm()
    if form.validate_on_submit():
        short_url = URLMap(
            short=form.custom_id.data,
            original=form.original_link.data
        )
        db.session.add(short_url)
        db.session.commit()
    return render_template('index.html', form=form)