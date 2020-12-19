from werkzeug.security import check_password_hash, generate_password_hash

from flash_learning import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    """Load a user from the database."""
    # print(User.query.get(1))
    return User.query.filter_by(alternative_id=id).first()



class User(UserMixin, db.Model):
    """Student data model."""

    __tablename__ = 'usertable'
    #static key for user
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    #login key for user, changed when changing password
    alternative_id = db.Column(db.Integer,index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    username = db.Column(db.String(64), index=True, unique=True)
    grade = db.Column(db.Integer, index=True)
    school = db.Column(db.String(100), index=True)
    activated = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password: str) -> None:
        """Hash the user's password before storing it in the database."""

        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> None:
        """Check the password hash from the database against the given password."""

        return check_password_hash(self.password, password)
    def get_id(self):
        return self.alternative_id


