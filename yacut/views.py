import random, re

from flask import render_template, request, redirect, flash, abort

from yacut import app, db
from .forms import CutForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CutForm()
    result_link = ''
    if form.validate_on_submit():
        if not form.custom_id.data:
            custom_id = get_unique_short_id()
        elif re.match(app.config['USER_PATTERN'], form.custom_id.data) is None:
            flash('Max 16 symbols from a-Z,0-9')
            return render_template('index.html', form=form, result_link=result_link)
        elif URLMap.query.filter_by(short=form.custom_id.data).first() is not None:
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('index.html', form=form, result_link=result_link)
        else:
            custom_id = form.custom_id.data
        short_url = URLMap(
            short=custom_id,
            original=form.original_link.data
        )
        db.session.add(short_url)
        db.session.commit()
        result_link = app.config['PREFIX_URL'] + short_url.short
    return render_template('index.html', form=form, result_link=result_link)


@app.route('/<regex:slug>', methods=['GET'])
def result_link(slug):
    long_url = URLMap.query.filter_by(short=slug).first()
    if long_url is None:
        abort(404)
    return redirect(long_url.original), 302