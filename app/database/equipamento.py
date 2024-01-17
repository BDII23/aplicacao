from db_manager import get_pg_cursor

def sp_create_equipamento(in_descricao, in_tipo_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_equipamento', [in_descricao, in_tipo_id])

def sp_update_equipamento(in_id, in_descricao, in_tipo_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_equipamento', [in_id, in_descricao, in_tipo_id])

def sp_delete_equipamento(in_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_equipamento', [in_id])

def fn_read_equipamento():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_equipamento')
        return cursor.fetchall()

def fn_readone_equipamento(in_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_equipamento', [in_id])
        return cursor.fetchall()
