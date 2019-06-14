# application/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()


# Effectively, an application factory
def create_app(config_type):  # dev, test, prod
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')  # Build the path to the config file
    app.config.from_pyfile(configuration)  # Let Flask do the configuration
    db.init_app(app)
    bootstrap.init_app(app)  # Initialize bootstrap for prettier UI
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from application.catalog import main  # This imports Blueprint
    app.register_blueprint(main)

    from application.auth import authentication
    app.register_blueprint(authentication)

    return app
