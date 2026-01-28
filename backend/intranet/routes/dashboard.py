from flask import Blueprint, render_template, session, redirect, url_for

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.get("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login.login_page"))
    return "Willkommen im Dashboard!"
