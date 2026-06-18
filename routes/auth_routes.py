from flask import Blueprint, redirect , render_template, request, flash, session, url_for
from services import auth_service
from utils.decorators import login_required, admin_required, checkin_page_required

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


@auth_bp.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    senha = request.form.get("senha")

    dados = {
        "email": email,
        "senha": senha
    }
    
    resultado, erros, status = auth_service.login_sessao(dados)
    
    if erros:
        flash("Erro na operação", erros[0])
        return redirect(url_for("auth.login_page"))
    
        
    session["usuario_id"] = resultado["id"]
    session["nome"] = resultado["nome"]
    session["email"] = resultado["email"]
    session["perfil"] = resultado["perfil"] 

        
    return redirect(url_for("convidados.dashboard_page"))
    
@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("Você saiu")
    return redirect(url_for("auth.login_page"))


@auth_bp.route("/me", methods=["GET"])
@login_required
def me():
    usuario = {
        "id": session["usuario_id"],
        "nome": session["nome"],
        "email": session["email"],
        "perfil": session["perfil"]
    }
    
    return render_template("me.html", usuario=usuario)

@auth_bp.route("/usuarios/cadastrar", methods=["GET"])
@login_required
@admin_required
def cadastrar_page():
    return render_template("usuario.html")

@auth_bp.route("/usuarios/cadastrar", methods=["POST"])
@login_required
@admin_required
def cadastrar_post_page():
    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")
    perfil = request.form.get("perfil")

    if not nome or not email or not senha or not perfil:
        flash("Todos os campos são obrigatórios", "danger")
        return redirect(url_for("auth.cadastrar_page"))
    
    
    
    dados = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "perfil": perfil
    }
    
    _, erros, _ = auth_service.cadastrar(dados)
    
    if erros:
        flash(erros[0], "danger")
        return redirect(url_for("auth.cadastrar_page"))
    
    return redirect(url_for("convidados.listar_page"))