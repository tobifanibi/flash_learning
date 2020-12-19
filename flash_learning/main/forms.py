from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

from flash_learning.models.user import User


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField("Sign In")


class SignupForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    school = StringField(label='school', validators=[DataRequired()])
    grade = IntegerField('grade', validators=[DataRequired()])

    def validate_username(self, username):
        """Check if the username is already taken."""

        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        """Check if the email is already tied to an account."""

        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError("Please use a different email address.")
