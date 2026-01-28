from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///intranet.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    db.init_app(app)

    from .routes.api import api_bp
    from .routes.admin import admin_bp

    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(admin_bp)

    return app
