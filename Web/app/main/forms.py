from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, HiddenField
from wtforms.validators import Required


class NameForm(Form):
    product = SelectField(u'product')
    subproduct = SelectField('subproduct')
    issue = SelectField('issue')
    subissue = SelectField('subissue')
    company = SelectField('company')
    state = SelectField('state')
    submit = SubmitField('Submit')
