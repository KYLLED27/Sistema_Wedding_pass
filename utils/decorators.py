from functools import wraps
from flask import request, jsonify, session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Usuario não logado")
            return redirect(url_for("auth.login_page"))
        return f(*args, **kwargs)
    return wrapper

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if session["perfil"] != "admin":
            flash("Sem permisão")
            return redirect(url_for("auth.login_page"))
        return f(*args, **kwargs)
    return wrapper

def checkin_page_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if session["perfil"] not in ["admin", "recepcao"]:
            flash("Sem permisão")
            return redirect(url_for("auth.login_page"))
        return f(*args, **kwargs)
    return wrapper


