from db_manager import get_pg_cursor

def sp_create_tipo_componente(p_tipo):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_tipo_componente', [p_tipo])

def sp_delete_tipo_componente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_tipo_componente', [p_id])

def sp_update_tipo_componente(p_id, p_tipo):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_tipo_componente', [p_id, p_tipo])

def fn_read_tipo_componente():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_tipo_componente')
        return cursor.fetchall()

def fn_readone_tipo_componente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_tipo_componente', [p_id])
        return cursor.fetchall()
