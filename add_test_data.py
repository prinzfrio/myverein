# file: add_test_data.py (im Projekt-Root)
from backend.app import app
from backend.intranet.db import db
from backend.intranet.models import Mitglied

with app.app_context():
    m1 = Mitglied(vorname="Anna", nachname="Muster", email="anna@example.com")
    m2 = Mitglied(vorname="Peter", nachname="Beispiel", email="peter@example.com")

    db.session.add_all([m1, m2])
    db.session.commit()

    print("Testdaten eingefügt.")
