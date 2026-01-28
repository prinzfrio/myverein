from flask import Blueprint, jsonify

ping_bp = Blueprint("ping", __name__)

@ping_bp.get("/api/ping")
def ping():
    return jsonify({"status": "ok"})
