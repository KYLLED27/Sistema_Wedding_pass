def success(data=None, message="Sucesso na operação"):
    return {
        "success": True,
        "message": message,
        "data": data
    }
    
def error(message="Erro na operação", erro=None):
    return {
        "success": False,
        "message": message,
        "erro": erro or []
    }
    