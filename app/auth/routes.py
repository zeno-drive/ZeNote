from flask import render_template,request,redirect,flash,url_for
from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash 
from . import auth

#@auth.route("/register",methods=["GET","POST"])
@auth.route("/",methods=["GET","POST"])
def register():
    return render_template("hub.html")