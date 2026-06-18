from flask import Blueprint, Flask, redirect, url_for
from routes.convidado_routes import conv_bp
from routes.auth_routes import auth_bp
from config import SECRET_KEY

app = Flask(__name__)
app.register_blueprint(conv_bp)
app.register_blueprint(auth_bp)
app.secret_key = SECRET_KEY

@app.route("/")
def home():
    return redirect(url_for("auth.login_page"))

if __name__ == "__main__":
    app.run(debug=True)