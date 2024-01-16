from .db_manager import get_pg_cursor

def sp_create_armazem(p_endereco):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_armazem', [p_endereco])

def sp_update_armazem(p_id, p_endereco):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_armazem', [p_id, p_endereco])

def sp_delete_armazem(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_armazem', [p_id])

def fn_read_armazem():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_armazem')
        return cursor.fetchall()

def fn_readone_armazem(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_armazem', [p_id])
        return cursor.fetchall()
