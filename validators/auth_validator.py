def validar_nome(nome):
    if not nome:
        return "Nome é obrigatório"
    if len(nome.strip()) < 3:
        return "Nome deve ser maior que 3 caracteres"
    return None

def validar_email(email):
    if not email:
        return "E-mail é obrigatório"
    if "@" not in email or "." not in email:
        return "E-mail deve ser valido"
    return None

def validar_senha(senha):
    if not senha:
        return "Senha é obrigatória"
    if len(senha) < 6:
        return "Senha deve conter no minimo 6 caracteres ou digitos"
    return None

def validar_perfil(perfil):
    if not perfil:
        return "Perfil é obrigatório"
    if perfil not in ["admin", "recepcao"]:
        return "Perfil deve ser admin ou recepcao"
    return None

def validar_usuario(dados):
    erros = []
    
    for erro in [
        validar_nome(dados.get("nome")),
        validar_email(dados.get("email")),
        validar_senha(dados.get("senha")),
        validar_perfil(dados.get("perfil"))
    ]:
        if erro:
            erros.append(erro)
            
    return erros

def validar_login(dados):
    erros = []
    
    for erro in [
        validar_email(dados.get("email")),
        validar_senha(dados.get("senha"))
    ]:
        if erro:
            erros.append(erro)
            
    return erros