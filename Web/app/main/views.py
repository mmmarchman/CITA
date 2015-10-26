from flask import Flask, render_template, request, g, flash
from flask.ext.login import login_required, current_user
from wtforms import Form, FloatField, BooleanField, TextField, validators
from . import main
import forms
import sqlite3
from .. import models
from Parser import Parser
import os


def get_connection():

    # Combines current working directory with the name of the db
    # so that we can operate on multiple platforms
    cwd = os.getcwd()

    output_file = open('outputFile.txt','rw+')
    db_location = os.path.join(cwd, 'data-dev.sqlite')
    output_file.write(db_location)
    conn = sqlite3.connect(db_location)
    output_file.close()
    return conn


def dictionary_factory(cursor, row):
    col_names = [d[0].lower() for d in cursor.description]
    return dict(zip(col_names, row))


@main.before_request
def before_request():
    g.user = current_user.get_id()

    if current_user.is_authenticated:
        g.companyid = current_user.company_id

    g.citadb = get_connection()


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile', methods=['GET','POST'])
def profile():
    if request.method == 'POST':
        flash ('The CITA development team can be reached at 404-368-0014 or via email: CITA@CITA.com')
    conn = get_connection()
    form = forms.ProfileForm(request.form)
    form.username.data = current_user.username
    form.companyname.data = "CS4850"
    form.email.data = current_user.email
    return render_template('profile.html', form=form)


@main.route('/trends', methods=['GET','POST'])
@login_required
def trends():
    conn = get_connection()
    #conn.text_factory = str
    form = forms.NameForm(request.form)
    form.product.choices = [("%", "ALL")] + [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='product').order_by('column_values')]
    form.subproduct.choices = [("%", "ALL")] + [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='subproduct').order_by('column_values')]
    form.issue.choices = [("%", "ALL")] + [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='issue').order_by('column_values')]
    form.subissue.choices = [("%", "ALL")] + [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='subissue').order_by('column_values')]
    form.company.choices = [("%", "ALL")] + [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='company').order_by('column_values')]
    form.state.choices = [("%", "ALL")] + [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='state').order_by('column_values')]
    return render_template('trends.html', form=form)


@main.route('/history')
@login_required
def history():
    return render_template('history.html')


@main.route('/datamanagement')
@login_required
def datamanagement():
    return render_template('datamanagement.html')


@main.route('/devtest', methods=['GET', 'POST'])
@login_required
def devtest():
    conn = get_connection()
    conn.text_factory = str
    form = forms.NameForm(request.form)    
    if request.method == 'POST':
        query = "select customer_complaint from a_data"
        andflag = 0
        if form.product.data != "%":
            query = query + " where product = '" + form.product.data + "'"
            andflag = 1
        if form.subproduct.data != "%":
            if andflag == 1:
                query = query + " and "
            else:
                query = query + " where "
                andflag = 1
            query = query + "subproduct = '" + form.subproduct.data + "'"
        if form.issue.data != "%":
            if andflag == 1:
                query = query + " and "
            else:
                query = query + " where "
                andflag = 1
            query = query + "issue = '" + form.issue.data + "'"
        if form.subissue.data != "%":
            if andflag == 1:
                query = query + " and "
            else:
                query = query + " where "
                andflag = 1
            query = query + "subissue = '" + form.subissue.data + "'"
        if form.company.data != "%":
            if andflag == 1:
                query = query + " and "
            else:
                query = query + " where "
                andflag = 1
            query = query + "company = '" + form.company.data + "'"
        if form.state.data != "%":
            if andflag == 1:
                query = query + " and "
            else:
                query = query + " where "
                andflag = 1
            query = query + "state = '" + form.state.data + "'"
        
        resultlist = conn.execute(query).fetchall()
        testlist = []
        for r in resultlist:
            for e in r:
                if e != None:
                    testlist.append(str(e))
        parse = Parser(testlist, 20)
        freq_dist = parse.parse()
        #flash(u"Initial SQL query results: %s" % resultlist)
        #flash(u"Convertion removes null, decodes, converts to list of strings: %s" %testlist)
        #flash(u"Parse results: %s" %freq_dist)
        return render_template('devtest.html', freq_dist=freq_dist)


