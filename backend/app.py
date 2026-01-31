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


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myverein.db"
app.config["SECRET_KEY"] = "irgendein_geheimer_schlüssel"

db.init_app(app)

app.register_blueprint(login_bp)
app.register_blueprint(mitglieder_bp)
app.register_blueprint(termine_bp)
app.register_blueprint(import_bp)
app.register_blueprint(ping_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(auth_bp)

@app.get("/")
def index():
    return redirect("/login")

@app.get("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login.login_page"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)