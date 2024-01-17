from db_manager import get_pg_cursor

def sp_delete_estado_guia_remessa(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_estado_guia_remessa', [p_id])

def sp_create_estado_guia_remessa(p_estado):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_estado_guia_remessa', [p_estado])

def sp_update_estado_guia_remessa(p_id, p_estado):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_estado_guia_remessa', [p_id, p_estado])

def fn_read_estado_guia_remessa():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_estado_guia_remessa')
        return cursor.fetchall()

def fn_readone_estado_guia_remessa(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_estado_guia_remessa', [p_id])
        return cursor.fetchall()