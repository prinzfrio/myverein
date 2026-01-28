from flask import Blueprint, request, jsonify

import_bp = Blueprint("import", __name__)

@import_bp.post("/api/import/prowinner")
def import_prowinner():
    file = request.files["file"]
    # Datei verarbeiten …
    return jsonify({"status": "ok"})
