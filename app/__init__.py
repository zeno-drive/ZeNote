from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
from .config import Config
from app.models import get_random_quote

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
    @login_manager.user_loader
    def load_user(user_id):
        from bson import ObjectId
        from app.models import User
        user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return User(user_data) if user_data else None
    @app.context_processor
    def inject_quote():
        return {"quote": get_random_quote()}

    return app


