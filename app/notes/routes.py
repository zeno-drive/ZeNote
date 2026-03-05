from flask import render_template, request, redirect, flash, url_for
from app import mongo
from . import notes
from app.models import User
from flask_login import login_required, current_user
from bson import ObjectId
from datetime import datetime


@notes.route("/note_editor/<note_id>", methods=["POST", "GET"])
@login_required
def note_editor(note_id):
    note = mongo.db.notes.find_one({"_id": ObjectId(note_id)})
    if request.method == "GET":
        return render_template("note_editor.html", note_id=note_id, note=note)
    else:
        content = request.form.get("content")
        mongo.db.notes.update_one(
            {"_id": ObjectId(note_id)},
            {"$set": {"content": content, "modified_at": datetime.now()}},
        )
        return redirect(url_for("notes.note_editor", note_id=note_id))
