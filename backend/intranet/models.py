from werkzeug.security import generate_password_hash, check_password_hash
from .db import db
from flask_login import UserMixin
#from ..db import db
from datetime import date

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="public")  # public, uebungsleiter, admin

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Termin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(100), nullable=False)
    beschreibung = db.Column(db.Text, nullable=True)
    datum = db.Column(db.Date, nullable=False, default=date.today)
    uhrzeit = db.Column(db.String(10), nullable=True)  # z.B. "19:30"
    ort = db.Column(db.String(100), nullable=True)

    # Sichtbarkeit
    public = db.Column(db.Boolean, default=True)    # öffentlich sichtbar
    intern = db.Column(db.Boolean, default=False)   # nur ÜL/Admin

    def __repr__(self):
        return f"<Termin {self.titel} am {self.datum}>"


class Mitglied(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vorname = db.Column(db.String(100))
    nachname = db.Column(db.String(100))
    email = db.Column(db.String(200))

class Benutzer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(200))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
