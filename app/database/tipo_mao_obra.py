from db_manager import get_pg_cursor

def sp_delete_tipo_mao_obra(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_tipo_mao_obra', [p_id])

def sp_create_tipo_mao_obra(p_tipo, p_custo):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_tipo_mao_obra', [p_tipo, p_custo])

def sp_update_tipo_mao_obra(p_id, p_tipo, p_custo):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_tipo_mao_obra', [p_id, p_tipo, p_custo])

def fn_read_tipo_mao_obra():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_tipo_mao_obra')
        return cursor.fetchall()

def fn_readone_tipo_mao_obra(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_tipo_mao_obra', [p_id])
        return cursor.fetchall()
