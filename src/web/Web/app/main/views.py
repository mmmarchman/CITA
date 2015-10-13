from flask import render_template
from flask.ext.login import login_required
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/trends')
@login_required
def trends():
    return render_template('trends.html')

