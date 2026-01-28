from app import app
from intranet import db

with app.app_context():
    db.create_all()
