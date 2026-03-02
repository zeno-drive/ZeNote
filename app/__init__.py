from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
from .config import Config

mongo = PyMongo()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    login_manager.init_app(app)

    from .auth import auth
    from .notes import notes
    from .folders import folders

    app.register_blueprint(auth)
    app.register_blueprint(notes)
    app.register_blueprint(folders)

    return app