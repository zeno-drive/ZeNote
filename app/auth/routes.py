from flask import render_template,request,redirect,flash,url_for
from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash 
from . import auth
from app.models import passwordvalid
@auth.route("/",methods=["GET","POST"])
def hub():
    return render_template("hub.html")

@auth.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        password=request.form.get("password")
        re_password=request.form.get("re_password")
        if password != re_password:
            return render_template("register.html",e="Confirm Password not same")
        try:
            passwordvalid(password)
        except ValueError as e:
            return render_template("register.html",e=e)
        if mongo.db.users.find_one({"email": email}):
            return render_template("register.html",e="Email already registered")
        hash=generate_password_hash(password)
        user={"name": name,"email": email,"hash": hash}
        mongo.db.users.insert_one(user)
        return render_template("hub.html",e=f"{hash}")
        
    
    return render_template("register.html",e=None)
@auth.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        if mongo.db.users.find_one({"email": email}):
            user=mongo.db.users.find_one({"email": email})
            if check_password_hash (user["hash"],password):
                return render_template("register.html",e=f"{hash}")
            else:
                return render_template("login.html",e=f"password or email was wrong")
        else:
            return render_template("login.html",e=f"email not registered")
        
    else:
        return render_template("login.html",e=None)