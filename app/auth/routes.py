from flask import render_template, request, redirect, flash, url_for
from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from app.models import passwordvalid, User
from flask_login import login_user, logout_user, login_required, current_user


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.hub"))


@auth.route("/")
def hub():
    if current_user.is_authenticated:
        return redirect(url_for("folders.dashboard"))
    else:
        return render_template("hub.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        re_password = request.form.get("re_password")
        if password != re_password:
            return render_template("register.html", e="Confirm Password not same")
        try:
            passwordvalid(password)
        except ValueError as e:
            return render_template("register.html", e=e)
        if mongo.db.users.find_one({"email": email}):
            return render_template("register.html", e="Email already registered")
        hash = generate_password_hash(password)
        user = {"name": name, "email": email, "hash": hash}
        mongo.db.users.insert_one(user)
        user_data = mongo.db.users.find_one({"email": email})
        login_user(User(user_data))
        return redirect(url_for("folders.dashboard"))
    return render_template("register.html", e=None)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = mongo.db.users.find_one({"email": email})
        if user:
            if check_password_hash(user["hash"], password):
                login_user(User(user))
                return redirect(url_for("folders.dashboard"))
            else:
                return render_template("login.html", e=f"Invalid password or email")
        else:
            return render_template("login.html", e=f"Invalid password or email")

    else:
        if current_user.is_authenticated:
            return redirect(url_for("folders.dashboard"))
    return render_template("login.html", e=None)
