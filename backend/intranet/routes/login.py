from flask import Blueprint, request, jsonify, session, render_template
from ..models import Benutzer
from ..db import db
from flask import redirect, url_for


login_bp = Blueprint("login", __name__)

# Login
@login_bp.post("/api/login")
def login():
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
