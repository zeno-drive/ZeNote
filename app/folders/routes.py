from flask import render_template, request, redirect, flash, url_for
from app import mongo
from . import folders
from app.models import User
from flask_login import login_required, current_user
from bson import ObjectId
from datetime import datetime


@folders.route("/dashboard", methods=["POST", "GET"])
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


@folders.route("/delete_folder", methods=["POST"])
@login_required
def delete_folder():
    folder_id = request.form.get("folder_id")
    mongo.db.notes.delete_many({"folder_id": ObjectId(folder_id)})
    mongo.db.folders.delete_one({"_id": ObjectId(folder_id)})
    return redirect(url_for("folders.dashboard"))


@folders.route("/folder_hub/<folder_id>", methods=["GET", "POST"])
@login_required
def folder_hub(folder_id):
    folder = mongo.db.folders.find_one({"_id": ObjectId(folder_id)})
    folder_notes = mongo.db.notes.find({"folder_id": ObjectId(folder_id)})
    if request.method == "GET":
        return render_template(
            "folder_hub.html", folder=folder, folder_notes=folder_notes, e=None
        )

    else:
        note_name = request.form.get("name").lower().strip()
        tags = [tag.lower().strip() for tag in request.form.get("tags").split(",")]
        if mongo.db.notes.find_one(
            {"name": note_name, "folder_id": ObjectId(folder_id)}
        ):
            return render_template(
                "folder_hub.html",
                folder=folder,
                folder_notes=folder_notes,
                e=f"note with name {note_name} already exists",
            )
        ct = datetime.now()
        note = {
            "user_id": ObjectId(current_user.id),
            "name": note_name,
            "tags": tags,
            "folder_id": ObjectId(folder_id),
            "modified_at": ct,
            "created_at": ct,
        }

        mongo.db.notes.insert_one(note)
        return redirect(url_for("folders.folder_hub", folder_id=folder_id))


@folders.route("/delete_note", methods=["POST"])
@login_required
def delete_note():
    note_id = request.form.get("note_id")
    note = mongo.db.notes.find_one({"_id": ObjectId(note_id)})
    folder_id = note["folder_id"]
    mongo.db.notes.delete_one({"_id": ObjectId(note_id)})
    return redirect(url_for("folders.folder_hub", folder_id=folder_id))
