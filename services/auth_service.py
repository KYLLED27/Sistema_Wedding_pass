from repositorys import usuario_repository
from utils.auth import verificar_senha, gerar_hash_senha
from validators.auth_validator import validar_usuario, validar_login


def cadastrar(dados):
    erros = validar_usuario(dados)
    
    if erros:
        return None, erros, 400
    
    email = usuario_repository.buscar_por_email(dados.get("email"))
    if email:
        return None, ["E-mail já cadastrado"], 409
    
    senha = gerar_hash_senha(dados.get("senha"))
    
    novo_usuario = {
        "nome": dados.get("nome"),
        "email": dados.get("email"),
        "senha": senha,
        "perfil": dados.get("perfil")
    }
    
    usuario = usuario_repository.inserir(novo_usuario)
    
    return usuario , None, 201

def login_sessao(dados):
    erros = validar_login(dados)
    
    if erros:
        return None, erros, 400
    
    usuario = usuario_repository.buscar_por_email(dados.get("email"))
    if not usuario:
        return None, ["Usuário ou senha Incorretos"], 401
    
    if not verificar_senha(dados.get("senha"), usuario["senha"]):
        return None, ["Usuário ou senha Incorretos"], 401
    
    return usuario, None, 200
     
def listar():
    usuarios = usuario_repository.listar()
    return usuarios, None, 200

def buscar(id):
    usuario = usuario_repository.buscar_por_id(id)
    
    if not usuario:
        return None, ["Usuario não encontrado"], 404
    
    return usuario, None, 200


def atualizar(dados, id):
    usuario = usuario_repository.buscar_por_id(id)
    
    if not usuario:
        return None, ["Usuario não encontrado"], 404
    
    erros = validar_usuario(dados)
    
    if erros:
        return None, erros, 400
    
    if usuario_repository.buscar_por_email(dados.get("email"), id_ignorar=id):
        return None, ["E-mail já cadastrado"], 409
    
    atualizado = usuario_repository.atualizar(dados, id)
    
    return atualizado, None, 200

def excluir(id):
    usuario = usuario_repository.buscar_por_id(id)
    
    if not usuario:
        return None, ["Usuario não encontrado"], 404
    
    deletado = usuario_repository.excluir(id)
    
    return deletado, None, 200


