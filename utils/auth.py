# from datetime import datetime, timedelta
# from config import SECRET_KEY, JWT
import bcrypt
# import jwt


def gerar_hash_senha(senha):
    senha_byte = senha.encode("utf-8")
    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha_byte, salt)
    return senha_hash.decode("utf-8")

def verificar_senha(senha, senha_hash):
    senha_byte = senha.encode("utf-8")
    hash_byte = senha_hash.encode("utf-8")
    return bcrypt.checkpw(senha_byte, hash_byte)

# def gerar_token(dados):
#     payload = {
#         "id": dados.get("id"),
#         "nome": dados.get("nome"),
#         "email": dados.get("email"),
#         "perfil": dados.get("perfil"),
#         "exp": datetime.utcnow() + timedelta(hours=JWT)
#     }
    
#     token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
#     return token

# def decodificar_token(token):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         return payload, None
#     except jwt.ExpiredSignatureError:
#         return None, ["Token expirado"]
#     except jwt.InvalidTokenError:
#         return None, ["Token inválido"]