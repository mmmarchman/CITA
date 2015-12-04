from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, HiddenField
from wtforms.fields.html5 import DateField
from wtforms.validators import Required

from flask_admin.form.widgets import DatePickerWidget



class NameForm(Form):
    product = SelectField(u'Product')
    subproduct = SelectField('Subproduct')
    issue = SelectField('Issue')
    subissue = SelectField('Subissue')
    company = SelectField('Company')
    state = SelectField('State')
    start_date = DateField('Start Date', format='%Y-%m-%d', widget=DatePickerWidget())
    end_date = DateField('End Date', format='%Y-%m-%d',  widget=DatePickerWidget())
    submit = SubmitField('Submit')


class ProfileForm(Form):
    username = StringField('User Name')
    companyname = StringField('Company Name')
    email = StringField('Email')


class ResultsForm(Form):
    word = StringField('Word')
    count = StringField('Count')
