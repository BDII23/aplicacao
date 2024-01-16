from .db_manager import get_pg_cursor

def sp_create_cliente(p_email, p_senha, p_nome, p_nif):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_cliente', [p_email, p_senha, p_nome, p_nif])

def sp_update_cliente(p_id, p_email, p_senha, p_nome, p_nif):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_cliente', [p_id, p_email, p_senha, p_nome, p_nif])

def sp_delete_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_cliente', [p_id])

def fn_read_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_cliente')
        return cursor.fetchall()

def fn_readone_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_cliente', [p_id])
        return cursor.fetchone()
