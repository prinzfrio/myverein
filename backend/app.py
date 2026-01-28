from flask import Flask
from flask import render_template, session, redirect, url_for
from .intranet import db
from .intranet.routes.login import login_bp
from .intranet.routes.mitglieder import mitglieder_bp
from .intranet.routes.termine import termine_bp
from .intranet.routes.import_prowinner import import_bp
from .intranet.routes.ping import ping_bp
from .intranet.routes.dashboard import dashboard_bp
from .intranet.routes.auth import auth_bp


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

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)



@app.get("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login.login_page"))
    return render_template("dashboard.html")


@app.get("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login.login_page"))

