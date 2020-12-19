from flask import Blueprint, render_template
from flask_login import login_required

students = Blueprint("student", __name__)

user = {
    "name": "Dory The Fish",
    "username": "LostDory",
    "grade": 8,
    "school": "School Of Fish"
}

scores = [
    {
        "username": "LostDory",
        "points": 10
    },
    {
        "username": "Nemo",
        "points": 21
    },
    {
        "username": "Kowalski",
        "points": 100
    },
    {
        "username": "Skipper",
        "points": 1
    }
]


@students.route("/student/<username>/home", methods=["GET"])
@login_required
def home(username):
    return render_template("home.html", title="Home", user=user)


@students.route("/student/<username>/profile", methods=["GET"])
@login_required
def profile(username):
    return render_template("profile.html", title="Profile", user=user)


@students.route("/student/<username>/stats", methods=["GET"])
@login_required
def stats(username):
    return render_template("stats.html", title="Stats", user=user)


@students.route("/student/<username>/leaderboard", methods=["GET"])
@login_required
def leaderboard(username):
    return render_template("leaderboard.html", title="Leaderboard", scores=scores)
