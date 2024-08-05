from http import HTTPStatus

from flask import flash, redirect, render_template

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('add_url.html', form=form)

    short_id = form.custom_id.data
    if short_id is None or short_id == '':
        short_id = get_unique_short_id()
    else:
        if URLMap.query.filter_by(short=short_id).first():
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('add_url.html', form=form)

    url_in_db = URLMap(
        original=form.original_link.data,
        short=short_id
    )
    db.session.add(url_in_db)
    db.session.commit()
    return render_template('add_url.html', form=form, url_in_db=url_in_db)


@app.route('/<short_id>')
def redirect_view(short_id):
    url_in_db = URLMap.query.filter_by(short=short_id).first_or_404().original
    return redirect(url_in_db, code=HTTPStatus.FOUND)
