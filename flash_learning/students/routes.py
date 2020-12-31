from flask import Blueprint, render_template
from flask_login import current_user, login_required

from flash_learning import db
from flash_learning.models.flashcard import Grade, Subject
from flash_learning.models.student import Student


# dummy variable for total number of Flashcards
# This will be updated once flashcard backend has been fleshed out
total_flashcards = 1000


students = Blueprint("student", __name__)


@students.route("/student/<username>/home", methods=["GET"])
@login_required
def home(username):
    # Get the subjects for the student's grade level.
    student = Student.query.filter_by(username=current_user.username).first()
    grade_id = db.session.query(Grade).filter(Grade.grade == student.grade).first().id
    subjects = Subject.query.filter_by(grade_id=grade_id).all()

    return render_template("home.html", title="Home", user=student, subjects=subjects)


@students.route("/student/<username>/profile", methods=["GET"])
@login_required
def profile(username):

    # Obtain the student username
    student = Student.query.filter_by(username=current_user.username).first()

    # Obtain the student school name, or default to None
    school_value = Student.query.filter_by(username=current_user.school).first()
    school_name = school_value if school_value else 'None'

    # Create a dictionary of shorthand grade levels used by the database and human readable equivalents to display on the UI
    grade_conversion = {'K': 'Kindergarden', '1': '1st', '2': '2nd', '3': '3rd', '4': '4th', '5': '5th', '6': '6th', '7': '7th', '8': '8th'}

    # Convert raw student grade in the database to human readable equivalent, else default to the raw grade
    grade = grade_conversion[current_user.grade] if current_user.grade in grade_conversion else current_user.grade

    return render_template("profile.html", title="Profile", user=student, school_name = school_name, grade=grade)


@students.route("/student/<username>/stats", methods=["GET"])
@login_required
def stats(username):
    student = Student.query.filter_by(username=current_user.username).first()
    score = current_user.points
    accuracy = "{0:.0%}".format(int(current_user.flashcards_correct) / int(current_user.flashcards_attempted))
    progress = "{0:.0%}".format(int(current_user.flashcards_attempted) / total_flashcards)
    return render_template("stats.html", title="Stats", user=student, score=score, accuracy=accuracy, progress=progress)


@students.route("/student/<username>/leaderboard", methods=["GET"])
@login_required
def leaderboard(username):
    student = Student.query.filter_by(username=current_user.username).first()

    # Returns the top 10 scores of the Stats database in descending order.
    scores = Student.query.order_by(Student.points.desc()).limit(10).all()
    return render_template("leaderboard.html", title="Leaderboard", scores=scores, user=student)
