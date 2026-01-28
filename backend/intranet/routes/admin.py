from flask import Blueprint

admin_bp = Blueprint("admin", __name__)

@admin_bp.get("/")
def dashboard():
    return "Admin Dashboard"

"""
from flask import Blueprint, render_template

admin_bp = Blueprint("admin", __name__)

@admin_bp.get("/")
def dashboard():
    return render_template("admin/dashboard.html")

"""


