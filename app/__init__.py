from flask import Flask
from .extensions import db

def create_app(static_folder="static", template_folder="templates"):
    app = Flask(__name__, instance_relative_config=True,
                static_folder=static_folder,
                template_folder=template_folder)
    app.config.from_object("config.Config")

    db.init_app(app)

    # import routes AFTER db is initialized
    from .routes import main
    app.register_blueprint(main)

    # import models so tables are created
    from . import models  

    return app

from .routes import main
from .auth import auth   # 👈 import auth blueprint

def create_app():
    app = Flask(__name__, instance_relative_config=True,
                template_folder="../templates",
                static_folder="../static")
    app.config.from_object("config.Config")

    from .extensions import db, login_manager
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
