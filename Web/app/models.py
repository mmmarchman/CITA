from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db, login_manager

class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    company_id = db.Column(db.Integer)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

    def __int__(self, username, email, pw, companyid):
        self.username = username
        self.email = email
        self.password = pw
        self.company_id = companyid

    def insertUser(user_name, email, password, companyid):
        user = User(user_name, email, password, companyid)
        db.session.add(user)
        db.session.commit()
        return


class AData(db.Model):
    __tablename__='a_data'
    complaint_id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'))
    date = db.Column(db.Date)
    product = db.Column(db.String(128))
    subproduct = db.Column(db.String(128))
    issue = db.Column(db.String(128))
    subissue = db.Column(db.String(128))
    customer_complaint = db.Column(db.String(512))
    company_response = db.Column(db.String(512))
    company = db.Column(db.String(128))
    state = db.Column(db.String(4))

    def __repr__(self):
        return '<AData %r>' % self.complaint_id

class Company(db.Model):
    __tablename__ = 'company'
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(128))
    contract_reference = db.Column(db.String(128))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    data_table = db.Column(db.String(128))

    def insertCompany(companyname, contractreference):
        company = Company(companyname, contractreference)
        db.session.add(company)
        db.session.commit()
        return

    def __repr__(self):
        return '<Company %r>' % self.company_name

    def __init__(self, companyname, contractreference):
        self.company_name = companyname
        self.contract_reference = contractreference

class StructuredData(db.Model):
    __tablename__='structured_data'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer)
    column_name = db.Column(db.String(128))
    column_values = db.Column(db.String(128))

    def __repr__(self):
        return '<StructuredData %r>' % self.id

class UnstructuredData(db.Model):
    __tablename__='unstructured_data'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'))
    column_name = db.Column(db.String(128))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
