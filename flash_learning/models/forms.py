from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Email
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')

class SignupForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired()])
    school =  StringField(label='school',validators=[DataRequired()])
    grade = IntegerField('grade',validators=[DataRequired()])

class User(UserMixin,db.Model):
    __tablename__ = 'usertable'
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(1000))
    grade = db.Column(db.Integer)
    school = db.Column(db.String(100), unique=True)


    def get_id(self):
        return self.alternative_id

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        self.authenticated=False
        return self.authenticated

    def get(self):
        return self



