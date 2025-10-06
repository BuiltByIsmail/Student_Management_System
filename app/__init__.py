from flask import Flask
from .extensions import db,  login_manager

from .routes import main
from .auth import auth   # 👈 import auth blueprint

def create_app(static_folder="static", template_folder="templates"):
    app = Flask(__name__, instance_relative_config=True,
                template_folder="../templates",
                static_folder="../static")
    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
