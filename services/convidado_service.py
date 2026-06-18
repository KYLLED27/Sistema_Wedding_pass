from repositorys import convidado_repository
from validators.convidado_validator import validar_convidado

def listar():
    convidados = convidado_repository.listar()
    return convidados, None, 200

def buscar_por_id(id):
    convidado = convidado_repository.buscar_por_id(id)
    
    if not convidado:
        return None, ["Convidado não encontrado"], 404
    
    return convidado, None, 200

def cadastrar(dados):
    erros = validar_convidado(dados)
    
    if erros:
        return None, erros, 400
    
    if convidado_repository.buscar_por_cpf(dados.get("cpf")):
        return None, ["CPF já cadastrado"], 409
    
    novo_convidado = {
       "nome": dados.get("nome"),
        "cpf": dados.get("cpf"),
        "mesa": dados.get("mesa")
    }
    
    convidado = convidado_repository.inserir(novo_convidado)
    
    return convidado, None, 201

def atualizar(dados, id):
    convidado = convidado_repository.buscar_por_id(id)
    
    if not convidado:
        return None, ["Convidado não encontrado"], 404
    
    erros = validar_convidado(dados)
    
    if erros:
        return None, erros, 400
    
    if convidado_repository.buscar_por_cpf(dados.get("cpf"), id_ignorar=id):
        return None, ["CPF já cadastrado"], 409
    
    atualizado = convidado_repository.atualizar(dados, id)
    
    return atualizado, None, 200

def excluir(id):
    convidado = convidado_repository.buscar_por_id(id)
    
    if not convidado:
        return None, ["Convidado não encontrado"], 404
    
    deletado = convidado_repository.excluir(id)
    
    return deletado, None, 200

def fazer_checkin(id):
    convidado = convidado_repository.buscar_por_id(id)
    
    if not convidado:
        return None, ["Convidado não encontrado"], 404
    
    if convidado["checkin"]:
        return None, ["Checkin já realizado"],409
    
    feito = convidado_repository.fazer_checkin(id)
    
    return feito, None, 200

def relatorio():
    convidados = convidado_repository.listar()
    total = len(convidados)
    confirmados = [c for c in convidados if c["checkin"]]
    pedentes = total - len(confirmados)
    
    return {
        "total": total,
        "confirmados": len(confirmados),
        "pendentes": pedentes
    }, None, 200
    
def pendentes():
    convidados = convidado_repository.listar()
    pendentes = [c for c in convidados if not c["checkin"]]
    return pendentes, None, 200