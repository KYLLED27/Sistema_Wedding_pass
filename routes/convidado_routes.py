from services import convidado_service
from flask import Blueprint, url_for, redirect, render_template, request, flash
from utils.decorators import login_required, admin_required, checkin_page_required

conv_bp = Blueprint("convidados", __name__)


@conv_bp.route("/dashboard", methods=["GET"])
@login_required
def dashboard_page():
    relatorio, _, _ = convidado_service.relatorio()
    return render_template("dashboard.html", relatorio=relatorio)

@conv_bp.route("/convidados", methods=["GET"])
@login_required
def listar_page():
    convidados, _, _ = convidado_service.listar()
    return render_template("convidados.html", convidados=convidados)

@conv_bp.route("/recepcao", methods=["GET"])
@login_required
def recepcao_page():
    pendentes, _, _ = convidado_service.pendentes()
    return render_template("recepcao.html", pendentes=pendentes)

@conv_bp.route("/convidados/cadastrar", methods=["GET"])
@login_required
@admin_required
def cadastrar_page():
    return render_template("cadastro.html")

@conv_bp.route("/convidados/cadastrar", methods=["POST"])
@login_required
@admin_required
def cadastrar_post_page():
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    mesa = request.form.get("mesa")
    
    if not nome or not cpf or not mesa:
        flash("Todos os campos são obrigatórios", "danger")
        return redirect(url_for("convidados.cadastrar_page"))
    
    if not mesa.isdigit():
        flash("Mesa deve ser um número", "danger")
        return redirect(url_for("convidados.cadastrar_page"))
    
    dados = {
        "nome": nome,
        "cpf": cpf,
        "mesa": int(mesa)
    }
    
    _, erros, _ = convidado_service.cadastrar(dados)
    
    if erros:
        flash(erros[0], "danger")
        return redirect(url_for("convidados.cadastrar_page"))
    
    return redirect(url_for("convidados.listar_page"))



@conv_bp.route("/convidados/<int:id>/editar", methods=["GET"])
@login_required
@admin_required
def editar_get_page(id):
    convidado, _, _ = convidado_service.buscar_por_id(id)
    
    return render_template("editar.html", convidado= convidado)

@conv_bp.route("/convidados/<int:id>/editar", methods=["POST"])
@login_required
@admin_required
def editar_post_page(id):
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    mesa = request.form.get("mesa")
    
    if not nome or not cpf or not mesa:
        flash("Todos os campos são obrigatórios", "danger")
        return redirect(url_for("convidados.editar_get_page", id= id))  
    if not mesa.isdigit():
        flash("Mesa deve ser um número", "danger")
        return redirect(url_for("convidados.editar_get_page", id= id))
    
    
    dados = {
        "nome": nome,
        "cpf": cpf,
        "mesa": int(mesa)
    }
    
    _, erros, _ = convidado_service.atualizar(dados, id)
    
    if erros:
        flash(erros[0], "danger")
        return redirect(url_for("convidados.editar_get_page", id= id))
    
    return redirect(url_for("convidados.listar_page"))

@conv_bp.route("/convidados/<int:id>/excluir", methods=["POST"])
@login_required
@admin_required
def excluir_page(id):
    _, erros, _ = convidado_service.excluir(id)
    
    if erros:
        flash(erros[0], "danger")
        return redirect(url_for("convidados.listar_page"))
    
    return redirect(url_for("convidados.listar_page"))

@conv_bp.route("/convidados/<int:id>/checkin", methods=["POST"])
@login_required
@checkin_page_required
def checkin_page(id):
    _, erros, _ = convidado_service.fazer_checkin(id)
    
    if erros:
        flash(erros[0], "danger")
        return redirect(url_for("convidados.listar_page"))
    
    return redirect(url_for("convidados.listar_page"))