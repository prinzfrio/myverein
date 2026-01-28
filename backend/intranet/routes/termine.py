from flask import Blueprint, request, jsonify

termine_bp = Blueprint("termine", __name__)

@termine_bp.get("/api/termine")
def get_termine():
    return jsonify([])
