from werkzeug.security import check_password_hash, generate_password_hash

from flash_learning import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    """Load a user from the database."""

    return User.query.get(int(id))


class User(UserMixin, db.Model):
    """Student data model."""

    __tablename__ = 'usertable'
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    username = db.Column(db.String(64), index=True, unique=True)
    grade = db.Column(db.Integer, index=True)
    school = db.Column(db.String(100), index=True)

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password: str) -> None:
        """Hash the user's password before storing it in the database."""

        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> None:
        """Check the password hash from the database against the given password."""

        return check_password_hash(self.password, password)

    """Returns an error when trying to sign in.
    def get_id(self):
        return self.alternative_id

    def get(self):
        return self
    """

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        self.authenticated=False
        return self.authenticated

