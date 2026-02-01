from flask import Flask
from flask import render_template, session, redirect, url_for

from backend.intranet import db
from backend.intranet.routes.login import login_bp
from backend.intranet.routes.mitglieder import mitglieder_bp
from backend.intranet.routes.termine import termine_bp
from backend.intranet.routes.import_prowinner import import_bp
from backend.intranet.routes.ping import ping_bp
from backend.intranet.routes.dashboard import dashboard_bp
from backend.intranet.routes.auth import auth_bp
from backend.intranet.routes.public import public_bp

from backend.intranet.models import User

from flask_login import LoginManager


# ---------------------------------------------------------
# 1. App erstellen (MUSS zuerst passieren!)
# ---------------------------------------------------------
app = Flask(__name__, template_folder="intranet/templates")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myverein.db"
app.config["SECRET_KEY"] = "irgendein_geheimer_schlüssel_habe_ich_mir_ueberlegt!"


# ---------------------------------------------------------
# 2. LoginManager initialisieren
# ---------------------------------------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login.login_page"


# 3. User Loader definieren 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ---------------------------------------------------------
# 4. Datenbank initialisieren
# ---------------------------------------------------------
db.init_app(app)


# ---------------------------------------------------------
# 5. Blueprints registrieren
# ---------------------------------------------------------
app.register_blueprint(public_bp)
app.register_blueprint(login_bp)
app.register_blueprint(mitglieder_bp)
app.register_blueprint(termine_bp)
app.register_blueprint(import_bp)
app.register_blueprint(ping_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(auth_bp)


@app.get("/")
def index():
    return redirect("/")

@app.get("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login.login_page"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)