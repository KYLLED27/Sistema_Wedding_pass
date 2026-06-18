from db import get_connection

def listar():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM convidados ORDER BY id DESC")
    dados = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return dados

def buscar_por_id(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM convidados WHERE id =%s", (id,))
    dado = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return dado

def buscar_por_cpf(cpf, id_ignorar=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    if id_ignorar:
        cursor.execute("SELECT * FROM convidados WHERE cpf =%s AND id !=%s ", (cpf, id_ignorar))
        dado = cursor.fetchone()
    else:
        cursor.execute("SELECT * FROM convidados WHERE cpf =%s ", (cpf,))
        dado = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return dado

def inserir(dados):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    sql = "INSERT INTO convidados (nome, cpf, mesa) VALUES (%s, %s, %s)"
    cursor.execute(sql, (dados.get("nome"), dados.get("cpf"), dados.get("mesa")))
    conn.commit()
    
    novo_id = cursor.lastrowid
    
    cursor.close()
    conn.close()
    
    return buscar_por_id(novo_id)



def atualizar(dados, id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    sql = "UPDATE convidados SET nome= %s, cpf= %s, mesa= %s WHERE id = %s"
    cursor.execute(sql, (dados.get("nome"), dados.get("cpf"), dados.get("mesa"), id,))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return buscar_por_id(id)

def fazer_checkin(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    sql = "UPDATE convidados SET checkin= True WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return buscar_por_id(id)

def excluir(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("DELETE FROM convidados WHERE id = %s", (id,))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return listar()