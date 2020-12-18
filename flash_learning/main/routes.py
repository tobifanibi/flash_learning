import os
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, current_user, logout_user
from werkzeug.urls import url_parse

from flash_learning.models.user import User
from flash_learning.models.forms import LoginForm,SignupForm
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
        return redirect(url_for("index"))

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

    # Something here is causing an internal server error when trying to load the login page.
    """
    if current_user.is_authenticated==False:
        form = LoginForm()
        return render_template('login.html', form=form)
        if form.validate_on_submit():
            user = User(form.username.data)
            user.alternative_id=os.urandom(16)
            user.authenticated = True
            login_user(user, remember=True)
            return render_template("index.html")
    else:
        return render_template("index.html")
    """


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

        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Welcome to Flash Learning!")
        return redirect(url_for("main.login"))

    return render_template("signup.html", title="Sign Up", form=form)

    """
    if request.form.get('email')==None and request.form.get('username')==None and request.form.get('password')==None and request.form.get('grade')==None and request.form.get('school')==None:
        print("Console User Entering Signup Page")
        return render_template("signup.html", form=form)

    if form.validate_on_submit()==False:
        print("Console User Sign Up Invalid")
        form.msg="Please Enter ALl Required Info"
        return render_template("signup.html", form=form)
    else:
        print("Checking if user Exist")
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        grade = request.form.get('grade')
        school = request.form.get('school')
        user = User.query.filter_by(email=email).first()

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        print("user exist")
        form = SignupForm()
        form.msg="A User With This Password or Username Exist"
        return render_template("signup.html", form=form)
    else:
        print("Adding User to Database")
        #password should be hashed
        new_user = User(email=email, username=username, password=password,grade=grade,school=school)
        db.session.add(new_user)
        db.session.commit()
        return index()
    """
