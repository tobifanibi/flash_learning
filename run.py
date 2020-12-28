import os

from sqlalchemy import exc

from flash_learning import create_app, db
from flash_learning.dummy_data import DummyData




####

import os
from flask import Blueprint, flash, redirect, render_template, request, url_for, session
from flask_login import login_user, current_user, logout_user,login_required
from flash_learning.models.student import Student
from flash_learning.main.forms import LoginForm,SignupForm
from flash_learning import db
from base64 import b64encode
from flash_learning.main.emailtask import create_confirmation_token, confirm_token
from flask_mail import Message

######


from flask import Blueprint, flash, redirect, render_template, request, url_for, session
app = create_app()
from flask_mail import Mail
mail = Mail(app)
email = Blueprint("email", __name__)
from flask import Blueprint, flash, redirect, render_template, request, url_for, session




@app.before_first_request
def create_tables():
    db.create_all()

    try:
        dummy_data = DummyData()
        dummy_data.populate_database()
    except exc.IntegrityError:
        db.session.rollback()



def send_email(user, subject, template):
    msg = Message(
        subject,
        recipients=[user],
        html=template,
        sender='flashlearning2020@outlook.com'
    )
    mail.send(msg)





@email.route('/signup', methods=['POST','GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = SignupForm()
    if form.validate_on_submit():
        user = Student(first_name=form.first_name.data,
                       last_name=form.last_name.data,
                       username=form.username.data,
                       grade=form.grade.data,
                       email=form.email.data,
                       password=form.password.data)
        alternative_id = b64encode(os.urandom(24)).decode('utf-8')
        while Student.query.filter_by(alternative_id=alternative_id).first()!=None:
            alternative_id = b64encode(os.urandom(24)).decode('utf-8')
        user.set_password(form.password.data)
        user.alternative_id=alternative_id
        login_user(user, remember=False)
        token = create_confirmation_token(user.email)
        confirm_url = url_for('email.confirm_email', token=token, _exmternal=True)
        html = render_template('confirm.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)
        login_user(user)
        flash('A confirmation email has been sent via email.', 'success')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("signup.html", title="Sign Up", form=form)

@email.route('/resend')
@login_required
def resend_confirmation():
    token = create_confirmation_token(current_user.email)
    confirm_url = url_for('email.confirm_email', token=token, _external=True)
    html = render_template('confirm.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(current_user.email, subject, html)
    flash('A new confirmation email has been sent.', 'success')
    return redirect(url_for('main.index'))

@email.route('/confirm/<token>', methods=['POST','GET'])
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('This Confirmation Email has expired')
        return redirect(url_for('main.index'))
    user = Student.query.filter_by(email=email).first()
    if user.activated:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.activated = True
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('main.index'))







if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.register_blueprint(email)
    app.run(debug=True, host='0.0.0.0', port=port)


