from flask import render_template,request,redirect,flash,url_for
from app import mongo
from . import folders
from app.models import User
from flask_login import login_required,current_user
from bson import ObjectId
from datetime import datetime

  
@folders.route("/dashboard",methods=["POST","GET"])
@login_required
def dashboard():
    user_folders = mongo.db.folders.find({"user_id": ObjectId(current_user.id)})
    if request.method=="GET":
        return render_template("dashboard.html",user_folders=user_folders)
        
    else:    
        folder_name=request.form.get("name")
        ct = datetime.now()
        folder={"user_id":ObjectId(current_user.id),"name":folder_name,"created_at":ct}
        
        mongo.db.folders.insert_one(folder)
        return redirect(url_for("folders.dashboard"))
    
    
    
            