from .db_manager import get_pg_cursor

def sp_delete_componente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_componente', [p_id])

def sp_create_componente(p_descricao, p_quantidade, p_tipo_id, p_armazem_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_componente', [p_descricao, p_quantidade, p_tipo_id, p_armazem_id])

def sp_update_componente(p_id, p_descricao, p_quantidade, p_tipo_id, p_armazem_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_componente', [p_id, p_descricao, p_quantidade, p_tipo_id, p_armazem_id])

def fn_read_componente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_componente', [p_id])
        return cursor.fetchall()

def fn_readone_componente():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_componente')
        return cursor.fetchall()
