import psycopg2
from psycopg2 import sql

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="bd2_trabalho_pratico",
    user="user",
    password="123"
)

# Criar um cursor para executar operações no banco de dados
cursor = conn.cursor()

# Procedimento armazenado para criar um armazém
def sp_create_armazem(p_endereco):
    call_sp_query = sql.SQL("CALL sp_create_armazem({});").format(sql.Literal(p_endereco))
    cursor.execute(call_sp_query)
    conn.commit()

# Procedimento armazenado para atualizar um armazém
def sp_update_armazem(p_id, p_endereco):
    call_sp_query = sql.SQL("CALL sp_update_armazem({}, {});").format(
        sql.Literal(p_id),
        sql.Literal(p_endereco)
    )
    cursor.execute(call_sp_query)
    conn.commit()

# Procedimento armazenado para deletar um armazém
def sp_delete_armazem(p_id):
    call_sp_query = sql.SQL("CALL sp_delete_armazem({});").format(sql.Literal(p_id))
    cursor.execute(call_sp_query)
    conn.commit()

# Procedimento armazenado para ler todos os armazéns
def fn_read_armazem():
    call_sp_query = sql.SQL("SELECT * FROM fn_read_armazem();")
    cursor.execute(call_sp_query)
    return cursor.fetchall()

# Procedimento armazenado para ler um armazém por ID
def fn_readone_armazem(p_id):
    call_sp_query = sql.SQL("SELECT * FROM fn_readone_armazem({});").format(sql.Literal(p_id))
    cursor.execute(call_sp_query)
    return cursor.fetchall()

# Fechar conexão
cursor.close()
conn.close()

