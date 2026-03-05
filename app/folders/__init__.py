from flask import Blueprint

folders = Blueprint("folders", __name__)


from . import routes
