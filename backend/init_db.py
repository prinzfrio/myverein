from app import app
from intranet.db import db

with app.app_context():
    db.create_all()
    print("Datenbank wurde initialisiert.")
