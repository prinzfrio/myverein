from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_user, logout_user, current_user
from backend.intranet.models import Benutzer
from backend.intranet.db import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.get("/register")
def register_page():
    return render_template("register.html")

@auth_bp.post("/api/register")
def register():
    data = request.form  # <-- wichtig!
    """
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    """

    username = data.get("username")
    password = data.get("password")

    if Benutzer.query.filter_by(username=username).first():
        return jsonify({"error": "Benutzer existiert bereits"}), 400

    user = Benutzer(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    #return redirect(url_for("auth.register_page"))
    return redirect(url_for("auth.register_page"))



@auth_bp.get("/login")
def login_page():
    return render_template("login.html")

@auth_bp.post("/api/login")
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = Benutzer.query.filter_by(username=username).first()

    # Benutzer existiert nicht oder Passwort falsch
    if not user or not user.check_password(password):
        return redirect(url_for("auth.login_page"))

    # Benutzer einloggen
    login_user(user)

    # Weiterleiten zum Dashboard
    return redirect(url_for("dashboard"))

@auth_bp.get("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login_page"))

