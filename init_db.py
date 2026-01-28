from backend.app import app
from backend.intranet.db import db

with app.app_context():
    db.create_all()
    print("Datenbank wurde initialisiert.")
