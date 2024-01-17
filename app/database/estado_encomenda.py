from db_manager import get_pg_cursor

def sp_create_estado_encomenda(p_data_criacao, p_estado):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_estado_encomenda', [p_data_criacao, p_estado])

def sp_update_estado_encomenda(p_id, p_data_criacao, p_estado):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_estado_encomenda', [p_id, p_data_criacao, p_estado])

def sp_delete_estado_encomenda(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_estado_encomenda', [p_id])

def fn_read_estado_encomenda():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_estado_encomenda')
        return cursor.fetchall()

def fn_readone_estado_encomenda(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_estado_encomenda', [p_id])
        return cursor.fetchall()
