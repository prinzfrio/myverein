from flask import Blueprint, request, jsonify, render_template
from backend.intranet.auth.roles import role_required
from flask_login import current_user
from backend.intranet.models import Termin


termine_bp = Blueprint("termine", __name__)

@termine_bp.get("/api/termine")
def get_termine():
    return jsonify([])

@termine_bp.get("/termine/neu")
@role_required("admin")
def termin_neu():
    return render_template("termin_neu.html")


@termine_bp.get("/termine")
def termine_page():
    if current_user.is_authenticated:
        if current_user.role == "uebungsleiter":
            termine = Termin.query.filter_by(intern=True).all()
        elif current_user.role == "admin":
            termine = Termin.query.all()
        else:
            termine = Termin.query.filter_by(public=True).all()
    else:
        termine = Termin.query.filter_by(public=True).all()

    return render_template("termine.html", termine=termine)
