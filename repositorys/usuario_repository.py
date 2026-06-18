from db import get_connection

def listar():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT id, nome, email, perfil FROM usuarios ORDER BY id DESC")
    dados = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return dados

def buscar_por_id(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT id, nome, email, perfil FROM usuarios WHERE id =%s", (id,))
    dado = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return dado

def buscar_por_email(email, id_ignorar=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    if id_ignorar:
        cursor.execute("SELECT * FROM usuarios WHERE email =%s and id != %s", (email, id_ignorar,))
        dado = cursor.fetchone()
    
    else:
        cursor.execute("SELECT * FROM usuarios WHERE email =%s", (email,))
        dado = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return dado

def inserir(dados):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    sql = "INSERT INTO usuarios (nome, email, senha, perfil) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (dados.get("nome"), dados.get("email"), dados.get("senha"), dados.get("perfil")))
    conn.commit()
    
    novo_id = cursor.lastrowid
    
    cursor.close()
    conn.close()
    
    return buscar_por_id(novo_id)



def atualizar(dados, id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    sql = "UPDATE usuarios SET nome= %s, email= %s, senha= %s, perfil= %s WHERE id = %s"
    cursor.execute(sql, (dados.get("nome"), dados.get("email"), dados.get("senha"),dados.get("perfil"), id,))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return buscar_por_id(id)


def excluir(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return listar()