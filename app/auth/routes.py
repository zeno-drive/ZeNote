from flask import render_template,request,redirect,flash,url_for
from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash 
from . import auth


@auth.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form.get("name")
        password=request.form.get("password")
        re_password=request.form.get("re_password")
        if password != re_password:
            return render_template("register.html",e="Confirm Password not same")
    
    return render_template("register.html",e=None)