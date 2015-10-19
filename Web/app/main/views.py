from flask import Flask, render_template, request, g, flash
from flask.ext.login import login_required
from wtforms import Form, FloatField, BooleanField, TextField, validators
from . import main
import forms
import sqlite3
from .. import models

def get_connection():
    
    # For local testing - C:/Users/McClain/Documents/GitHub/CITA/Web/data-dev.sqlite
    # For deployment on the LAMP Server - /var/www/html/CITA/Web/data-dev.sqlite
    conn = sqlite3.connect('/var/www/html/CITA/Web/data-dev.sqlite')
    return conn


def dictionary_factory(cursor, row):
    col_names = [d[0].lower() for d in cursor.description]
    return dict(zip(col_names, row))


@main.before_request
def before_request():
    g.citadb = get_connection()


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        flash('Something magical happens!')
    return render_template('profile.html')


@main.route('/trends', methods=['GET', 'POST'])
@login_required
def trends():
    if request.method == 'POST':
        flash('Work in Progress - popup should appear w/ results')
    conn = get_connection()
    form = forms.NameForm(request.form)
    form.product.choices = [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='product').order_by('column_values')]
    form.subproduct.choices = [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='subproduct').order_by('column_values')]
    form.issue.choices = [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='issue').order_by('column_values')]
    form.subissue.choices = [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='subissue').order_by('column_values')]
    form.company.choices = [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='company').order_by('column_values')]
    form.state.choices = [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='state').order_by('column_values')]
    return render_template('trends.html', form=form)


@main.route('/devtest', methods=['GET', 'POST'])
@login_required
def devtest():
    if request.method == 'POST':
        flash ('The CITA development team can be reached at 404-368-0014 or via email: CITA@CITA.com')
    conn = get_connection()
    form = forms.ProfileForm(request.form)
    #form.username.data
    #form.companyname.data
    #form.email.data
    return render_template('devtest.html', form=form)


