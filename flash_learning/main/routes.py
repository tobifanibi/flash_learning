import os
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, current_user, logout_user
from werkzeug.urls import url_parse

from flash_learning.models.user import User
from flash_learning.main.forms import LoginForm,SignupForm
from flash_learning import db


main = Blueprint("main", __name__)


@main.route('/', methods=["GET", "POST"])
def index():
    """The app's landing page."""

    return render_template("index.html")


@main.route('/login', methods=["GET", "POST"])
def login():
    """"Student login page."""

    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()

    # Redirect the student to their home page if username and password are correct, otherwise stay at the login page.
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("main.login"))
        login_user(user)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for("main.index")
        return redirect(next_page)

    return render_template("login.html", title="Sign In", form=form)




@main.route("/logout")
def logout():
    """Logout the current user."""
    logout_user()

    return redirect(url_for("main.index"))


@main.route('/signup',methods=['POST','GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = SignupForm()

    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    school=form.school.data,
                    grade=form.grade.data)
  
        user.alternative_id=os.urandom(16)
        user.set_password(form.password.data)
        login_user(user, remember=False)
        db.session.add(user)
        db.session.commit()
        flash("Welcome to Flash Learning!")
        return redirect(url_for("main.login"))

    return render_template("signup.html", title="Sign Up", form=form)


