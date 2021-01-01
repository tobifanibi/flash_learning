from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from flash_learning import db
from flash_learning.email.utils import send_email
from flash_learning.main.emailtask import confirm_token, create_confirmation_token
from flash_learning.models.student import Student


email = Blueprint("email", __name__)


@login_required
@email.route('/resend')
def resend_confirmation():
    token = create_confirmation_token(current_user.email)
    confirm_url = url_for('email.confirm_email', token=token, _external=True)
    html = render_template('confirm.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(current_user.email, subject, html)
    flash('A new confirmation email has been sent.', 'success')
    return redirect(url_for('main.index'))


@email.route('/confirm/<token>', methods=['POST', 'GET'])
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
