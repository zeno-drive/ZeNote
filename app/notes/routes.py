from flask import render_template, request, redirect, flash, url_for
from app import mongo
from . import folders
from . import notes
from app.models import User
from flask_login import login_required, current_user
from bson import ObjectId
from datetime import datetime




