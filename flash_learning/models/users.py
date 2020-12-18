from flash_learning import db
from flask_login import UserMixin
# Create a model for user
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(1000))
    grade = db.Column(db.Integer)
    school = db.Column(db.String(100), unique=True)

