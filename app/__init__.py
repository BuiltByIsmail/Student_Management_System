from flask import Flask
from .extensions import db, login_manager
from .routes import main
from .auth import auth
from . import models

def create_app(static_folder="static", template_folder="templates"):
    app = Flask(__name__, instance_relative_config=True,
                static_folder=static_folder,
                template_folder=template_folder)

    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app