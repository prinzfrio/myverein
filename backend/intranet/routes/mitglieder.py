from flask import Blueprint, request, jsonify
from ..models import Mitglied
from ..db import db

mitglieder_bp = Blueprint("mitglieder", __name__)

# Alle Mitglieder abrufen
@mitglieder_bp.get("/api/mitglieder")
def get_mitglieder():
    alle = Mitglied.query.all()
    return jsonify([
        {
            "id": m.id,
            "vorname": m.vorname,
            "nachname": m.nachname,
            "email": m.email
        }
        for m in alle
    ])

# Einzelnes Mitglied abrufen
@mitglieder_bp.get("/api/mitglieder/<int:id>")
def get_mitglied(id):
    m = Mitglied.query.get_or_404(id)
    return jsonify({
        "id": m.id,
        "vorname": m.vorname,
        "nachname": m.nachname,
        "email": m.email
    })

# Neues Mitglied anlegen
@mitglieder_bp.post("/api/mitglieder")
def create_mitglied():
    #data = request.json
    data = request.form

    neues = Mitglied(
        vorname=data.get("vorname"),
        nachname=data.get("nachname"),
        email=data.get("email")
    )

    db.session.add(neues)
    db.session.commit()

    return jsonify({"message": "Mitglied erstellt", "id": neues.id}), 201

# Mitglied aktualisieren
@mitglieder_bp.put("/api/mitglieder/<int:id>")
def update_mitglied(id):
    m = Mitglied.query.get_or_404(id)
    data = request.json

    m.vorname = data.get("vorname", m.vorname)
    m.nachname = data.get("nachname", m.nachname)
    m.email = data.get("email", m.email)

    db.session.commit()

    return jsonify({"message": "Mitglied aktualisiert"})

# Mitglied löschen
@mitglieder_bp.delete("/api/mitglieder/<int:id>")
def delete_mitglied(id):
    m = Mitglied.query.get_or_404(id)
    db.session.delete(m)
    db.session.commit()

    return jsonify({"message": "Mitglied gelöscht"})

