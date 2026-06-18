def validar_nome(nome):
    if not nome:
        return "Nome é obrigatório"
    if len(nome.strip()) < 3:
        return "Nome deve ser maior que 3 caracteres"
    return None

def validar_cpf(cpf):
    if not cpf:
        return "CPF é obrigatório"
    if len(cpf) != 11:
        return "CPF deve ser válido"
    if not cpf.isdigit():
        return "CPF deve ser digito"
    return None

def validar_mesa(mesa):
    if mesa is None:
        return "Mesa é obrigatória"
    if not isinstance(mesa, int):
        return "Mesa deve ser um numero inteiro"
    if mesa < 1:
        return "Mesa deve ser maior que 0"
    return None

def validar_convidado(dados):
    erros = []
    
    for erro in [
        validar_nome(dados.get("nome")),
        validar_cpf(dados.get("cpf")),
        validar_mesa(dados.get("mesa"))
    ]:
        if erro:
            erros.append(erro)
            
    return erros