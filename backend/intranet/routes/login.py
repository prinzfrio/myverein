from flask import Blueprint, request, jsonify, session, render_template
from ..models import Benutzer
from ..db import db
from flask import redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from backend.intranet.models import User

login_bp = Blueprint("login", __name__)

# Login
@login_bp.post("/login")
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        flash("Login fehlgeschlagen", "danger")
        return redirect("/login")

    login_user(user)
    return redirect("/dashboard")


@login_bp.post("/api/login")
def api_login():
    #data = request.json
    if request.is_json:
        data = request.json
    else:
        data = request.form

    user = Benutzer.query.filter_by(username=data["username"]).first()

    if user is None or not user.check_password(data["password"]):
        return jsonify({"error": "Ungültige Zugangsdaten"}), 401

    session["user_id"] = user.id
    #return jsonify({"message": "Login erfolgreich"})
    return redirect("/dashboard")


# Logout
@login_bp.post("/api/logout")
def logout():
    session.pop("user_id", None)
    return jsonify({"message": "Logout erfolgreich"})

@login_bp.get("/login")
def login_page():
    return render_template("login.html")
