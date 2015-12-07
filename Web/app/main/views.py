from flask import render_template, request, g, flash, redirect, url_for
import flask
from flask.ext.login import login_required, current_user
from ..decorators import admin_required, permission_required
from wtforms import Form, FloatField, BooleanField, TextField, validators
from wtforms.fields.html5 import DateField
from datetime import datetime
from . import main
from . import forms
import sqlite3
from .. import models
from .. import db
from .Parser import Parser
import os

def get_connection():
    # Combines current working directory with the name of the db
    # so that we can operate on multiple platforms
    basedir = os.path.abspath(os.path.dirname(__file__))

    db_location = os.path.join(basedir, 'data-dev.sqlite')
    conn = sqlite3.connect(db_location)

    return conn


def dictionary_factory(cursor, row):
    col_names = [d[0].lower() for d in cursor.description]
    return dict(zip(col_names, row))


@main.before_request
def before_request():
    flask.g.user = current_user.get_id()

    if current_user.is_authenticated:
        flask.g.companyid = current_user.company_id

    #g.citadb = get_connection()


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/cadmin', methods=['GET','POST'])
@login_required
def cadmin():
    companylist = models.Company.query.all()
    form = forms.AddCompanyForm(request.form)
    form.company_name.data = ''
    form.contract_reference.data = ''
    if request.method == 'POST':
        form = forms.AddCompanyForm(request.form)
        #company = models.Company(form.company_name, form.contract_reference)
        models.Company.insertCompany(form.company_name.data, form.contract_reference.data)
        return redirect(request.url)
    return render_template('cadmin.html', companylist=companylist, form=form)


@main.route('/uadmin', methods=['GET','POST'])
@login_required
def uadmin():
    userlist = models.User.query.all()
    form = forms.AddUserForm(request.form)
    form.user_company.choices = [("", "")] + [(c.company_id, c.company_name) for c in models.Company.query.all()]
    form.user_company.default = [("", "")]
    if request.method == 'POST':
        print('post')
        form = forms.AddUserForm(request.form)
        user = models.User(username = form.user_name.data, email = form.user_email.data, password = 'citanewuser', company_id = form.user_company.data)
        db.session.add(user)
        return redirect(request.url)
    return render_template('uadmin.html', userlist=userlist, form=form)


@main.route('/trends', methods=['GET','POST'])
@login_required
def trends():
    conn = get_connection()
    startdatequery = 'SELECT start_date FROM company WHERE company_id =' + str(flask.g.companyid)
    enddatequery = 'SELECT end_date FROM company WHERE company_id =' + str(flask.g.companyid)
    startdate = conn.execute(startdatequery).fetchone()
    enddate = conn.execute(enddatequery).fetchone()

    range1form = forms.DateRangeForm1(request.form)
    range1form.start_date1.data = datetime.strptime(startdate[0], '%Y-%m-%d')
    range1form.end_date1.data = datetime.strptime(enddate[0], '%Y-%m-%d')

    range2form = forms.DateRangeForm2(request.form)
    range2form.start_date2.data = datetime.strptime(startdate[0], '%Y-%m-%d')
    range2form.end_date2.data = datetime.strptime(enddate[0], '%Y-%m-%d')

    # IF G.COMPANY_ID == 1:
    form = forms.Company1Form(request.form)
    #form.start_date.data = datetime.strptime(startdate[0], '%Y-%m-%d')
    #form.end_date.data = datetime.strptime(enddate[0], '%Y-%m-%d')

    form.product.choices = [("%", "ALL")] + [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='product').order_by('column_values')]
    form.subproduct.choices = [("%", "ALL")] + [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='subproduct').order_by('column_values')]
    form.issue.choices = [("%", "ALL")] + [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='issue').order_by('column_values')]
    form.subissue.choices = [("%", "ALL")] + [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='subissue').order_by('column_values')]
    form.company.choices = [("%", "ALL")] + [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='company').order_by('column_values')]
    form.state.choices = [("%", "ALL")] + [(g.column_values, g.column_values) for g in models.StructuredData.query.filter(models.StructuredData.column_name =='state').order_by('column_values')]

    #IF G.COMPANY_ID == 2:
    # different forms

    return render_template('trends.html',form=form,startdate=startdate,enddate=enddate,range1form=range1form,range2form=range2form)


@main.route('/history')
@login_required
def history():
    return render_template('history.html')


@main.route('/datamanagement')
@login_required
def datamanagement():
    return render_template('datamanagement.html')


@main.route('/results', methods=['GET', 'POST'])
@login_required
def results():
    conn = get_connection()
    #conn.text_factory = str

    range1form = forms.DateRangeForm1(request.form)
    range2form = forms.DateRangeForm2(request.form)

    #IF G.COMPANY_ID == 1:
    form = forms.Company1Form(request.form)
    if request.method == 'POST':
        query1 = "select customer_complaint from a_data"
        andflag = 0
        if form.product.data != "%":
            query1 = query1 + " where product = '" + form.product.data + "'"
            andflag = 1
        if form.subproduct.data != "%":
            if andflag == 1:
                query1 = query1 + " and "
            else:
                query1 = query1 + " where "
                andflag = 1
            query1 = query1 + "subproduct = '" + form.subproduct.data + "'"
        if form.issue.data != "%":
            if andflag == 1:
                query1 = query1 + " and "
            else:
                query1 = query1 + " where "
                andflag = 1
            query = query1 + "issue = '" + form.issue.data + "'"
        if form.subissue.data != "%":
            if andflag == 1:
                query1 = query1 + " and "
            else:
                query1 = query1 + " where "
                andflag = 1
            query1 = query1 + "subissue = '" + form.subissue.data + "'"
        if form.company.data != "%":
            if andflag == 1:
                query1 = query1 + " and "
            else:
                query1 = query1 + " where "
                andflag = 1
            query1 = query1 + "company = '" + form.company.data + "'"
        if form.state.data != "%":
            if andflag == 1:
                query1 = query1 + " and "
            else:
                query1 = query1 + " where "
                andflag = 1
            query1 = query1 + "state = '" + form.state.data + "'"
        if andflag == 1:
            query1 = query1 + " and "
        else:
            query1 = query1 + " where "
        query2 = query1
        query1 = "{0} date BETWEEN \'{1}\' AND \'{2}\'".format(query1, str(range1form.start_date1._value()),
                                                               str(range1form.end_date1._value()))
        query2 = "{0} date BETWEEN \'{1}\' AND \'{2}\'".format(query2, str(range2form.start_date2._value()),
                                                               str(range2form.end_date2._value()))

        print(query1)
        print(query2)

        resultlist1 = conn.execute(query1).fetchall()
        resultlist2 = conn.execute(query2).fetchall()
        testlist1 = []
        testlist2 = []
        for r in resultlist1:
            for e in r:
                if e != None:
                    testlist1.append(str(e))
        for r in resultlist2:
            for e in r:
                if e != None:
                    testlist2.append(str(e))
        parse1 = Parser(testlist1, 20)
        parse2 = Parser(testlist2, 20)
        freq_dist1 = parse1.parse()
        freq_dist2 = parse2.parse()
        #flash(u"Initial SQL query results: %s" % resultlist)
        #flash(u"Convertion removes null, decodes, converts to list of strings: %s" %testlist)
        #flash(u"Parse results: %s" %freq_dist)
        range1start = range1form.start_date1._value()
        range1end = range1form.end_date1._value()
        range2start = range2form.start_date2._value()
        range2end = range2form.end_date2._value()
        return render_template('results.html',
                               freq_dist1=freq_dist1,
                               freq_dist2=freq_dist2,
                               range1start=range1start,
                               range1end=range1end,
                               range2start=range2start,
                               range2end=range2end,)