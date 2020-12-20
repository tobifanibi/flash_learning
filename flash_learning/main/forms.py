from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError

from flash_learning.models.student import Student


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField("Sign In")


class SignupForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    grade = IntegerField('grade', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        """Check if the username is already taken."""

        user = Student.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        """Check if the email is already tied to an account."""

        email = Student.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError("Please use a different email address.")
