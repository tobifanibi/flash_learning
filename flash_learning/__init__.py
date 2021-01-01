from typing import Type

from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from flash_learning.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

login_manager.login_view = "main.login"


def create_app(config_class: Type[Config] = Config) -> Flask:
    """
    Create an instance of the flask app.

    :param config_class: Configuration parameters.
    :return: The flask app.
    """

    # Create an instance of the flask app and set the app's configuration.
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize email server.
    mail.init_app(app)

    # Start up the app's database.
    db.init_app(app)

    # Attach the login manager to the app.
    login_manager.init_app(app)

    # Register blueprints (routes).
    from flash_learning.email.routes import email
    from flash_learning.main.routes import main
    from flash_learning.students.routes import students

    app.register_blueprint(email)
    app.register_blueprint(main)
    app.register_blueprint(students)

    return app
