from typing import Type
from datetime import timedelta
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from flash_learning.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "main.login"



def create_app(config_class: Type[Config] = Config) -> Flask:
    """
    Create an instance of the flask app; update its configuration; spins up the app's database; attaches to the login
    manager; and register its routes.

    :param config_class: Configuration parameters.
    :return: The flask app.
    """

    # Create an instance of the flask app and set the app's configuration.
    app = Flask(__name__)
    app.config.from_object(config_class)
    # Start up the app's database.
    db.init_app(app)

    # Attach the login manager to the app.
    login_manager.init_app(app)

    # Register blueprints (routes).
    from flash_learning.main.routes import main
    from flash_learning.students.routes import students
    app.register_blueprint(main)
    app.register_blueprint(students)

    return app
