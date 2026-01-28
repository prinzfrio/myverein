from flask import Blueprint, render_template, request, redirect, url_for, jsonify
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
