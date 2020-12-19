import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """A configurations class for the flask app."""

    SECRET_KEY = os.environ.get("SECRET_KEY") or b'\xbf\x1b\xe1\x18\xaf\x8b\x1a\xb2\xa6\xb9\xcf\x7f\xe0+\xda\xd9'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or f"sqlite:///{os.path.join(basedir, 'site.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
