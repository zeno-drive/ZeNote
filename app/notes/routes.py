from flask import render_template, request, redirect, flash, url_for
from app import mongo
from . import folders
from . import notes
from app.models import User
from flask_login import login_required, current_user
from bson import ObjectId
from datetime import datetime


@notes.route("/folder_hub", methods=["POST", "GET"])  # needschanges
@login_required
def dashboard():
    user_folders = mongo.db.folders.find({"user_id": ObjectId(current_user.id)})
    if request.method == "GET":
        return render_template("dashboard.html", user_folders=user_folders, e=None)

    else:
        folder_name = request.form.get("name").lower().strip()
        if mongo.db.folders.find_one({"name": folder_name}):
            return render_template(
                "dashboard.html",
                user_folders=user_folders,
                e=f"folder with name {folder_name} already exists",
            )
        ct = datetime.now()
        folder = {
            "user_id": ObjectId(current_user.id),
            "name": folder_name,
            "created_at": ct,
        }

        mongo.db.folders.insert_one(folder)
        return redirect(url_for("folders.dashboard"))


@notes.route("/delete_note", methods=["POST"])
@login_required
def delete_note():
    note_id = request.form.get("note_id")
    mongo.db.notes.delete_one({"_id": ObjectId(note_id)})
    return redirect(url_for("folders.dashboard"))
