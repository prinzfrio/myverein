from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)

@api_bp.get("/mitglieder")
def get_mitglieder():
    return jsonify({"status": "ok", "data": []})
