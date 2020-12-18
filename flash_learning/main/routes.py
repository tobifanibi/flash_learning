import os
from flask import Blueprint, render_template
from flask_login import login_user,current_user
from flash_learning.models.users import User
from flash_learning.models.forms import LoginForm,SignupForm
from flash_learning import db
from flask import request
main = Blueprint("main", __name__)



@main.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")


@main.route('/login', methods=['GET', 'POST'])
def login():
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

@main.route('/signup',methods=['POST','GET'])
def signup():
	form = SignupForm()
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
