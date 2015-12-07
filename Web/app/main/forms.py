from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, HiddenField, ValidationError
from wtforms.fields.html5 import DateField
from wtforms.validators import Required, Length, Regexp, Email
from ..models import User



class NameForm(Form):
    product = SelectField(u'Product')
    subproduct = SelectField('Subproduct')
    issue = SelectField('Issue')
    subissue = SelectField('Subissue')
    company = SelectField('Company')
    state = SelectField('State')
    submit = SubmitField('Submit')


class ProfileForm(Form):
    username = StringField('User Name')
    companyname = StringField('Company Name')
    email = StringField('Email')


class ResultsForm(Form):
    word = StringField('Word')
    count = StringField('Count')

class Company1Form(Form):
    start_date = DateField('Start Date', format='%Y-%m-%d')
    end_date = DateField('End Date', format='%Y-%m-%d')
    product = SelectField(u'Product')
    subproduct = SelectField('Subproduct')
    issue = SelectField('Issue')
    subissue = SelectField('Subissue')
    company = SelectField('Company')
    state = SelectField('State')
    submit = SubmitField('Submit')

class DateRangeForm1(Form):
    start_date1 = DateField('Start Date', format='%Y-%m-%d', validators=[Regexp('^[0-9]*4-[0-9]*2-[0-9]*2',0,'Date must be in format YYYY-MM-DD')])
    end_date1 = DateField('End Date', format='%Y-%m-%d')

class DateRangeForm2(Form):
    start_date2 = DateField('Start Date', format='%Y-%m-%d')
    end_date2 = DateField('End Date', format='%Y-%m-%d')

class AddCompanyForm(Form):
    company_name = StringField('Company Name:', validators=[Required()])
    contract_reference = StringField('Contract Reference:', validators=[Required()])
    submit = SubmitField('Submit')

class AddUserForm(Form):
    user_name = StringField('User Name:', validators=[Required(), Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'Usernames must have only letters, numbers, dots or underscores')])
    user_email = StringField('User Email:', validators=[Required(), Length(1,64), Email()])
    user_company = SelectField('User Company', validators=[Required()])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use!')