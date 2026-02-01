from flask import Blueprint, request, jsonify, render_template, redirect, flash

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

# Neues Mitglied – Formular anzeigen
@mitglieder_bp.get("/mitglieder/neu")
def mitglied_neu_page():
    return render_template("mitglied_neu.html")

# Neues Mitglied – Formular absenden
@mitglieder_bp.post("/mitglieder/neu")
def mitglied_neu_save():
    vorname = request.form.get("vorname")
    nachname = request.form.get("nachname")
    email = request.form.get("email")

    neues = Mitglied(
        vorname=vorname,
        nachname=nachname,
        email=email
    )

    db.session.add(neues)
    db.session.commit()

    flash("Neues Mitglied wurde angelegt.", "success")
    return redirect("/mitglieder")


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


# Bestätigungsseite anzeigen
@mitglieder_bp.get("/mitglieder/<int:id>/delete")
def delete_mitglied_confirm(id):
    m = Mitglied.query.get_or_404(id)
    return render_template("mitglied_delete.html", m=m)

# Löschung durchführen (POST)
@mitglieder_bp.post("/mitglieder/<int:id>/delete")
def delete_mitglied_confirmed(id):
    m = Mitglied.query.get_or_404(id)
    db.session.delete(m)
    db.session.commit()
    flash("Mitglied wurde gelöscht.", "danger")
    return redirect("/mitglieder")


# HTML-Seite: Mitglieder anzeigen
@mitglieder_bp.get("/mitglieder")
def mitglieder_page():
    alle = Mitglied.query.all()
    return render_template("mitglieder.html", mitglieder=alle)

# Mitglied bearbeiten – Formular anzeigen
@mitglieder_bp.get("/mitglieder/<int:id>/edit")
def edit_mitglied_page(id):
    m = Mitglied.query.get_or_404(id)
    return render_template("mitglied_edit.html", m=m)

# Mitglied bearbeiten – Formular absenden
@mitglieder_bp.post("/mitglieder/<int:id>/edit")
def edit_mitglied_save(id):
    m = Mitglied.query.get_or_404(id)

    m.vorname = request.form.get("vorname")
    m.nachname = request.form.get("nachname")
    m.email = request.form.get("email")

    db.session.commit()
    flash("Mitglied erfolgreich aktualisiert.", "success")
    return redirect("/mitglieder")



