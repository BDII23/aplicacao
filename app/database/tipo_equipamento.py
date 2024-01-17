from django.db import connections

def sp_create_tipo_equipamento(p_tipo):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_tipo_equipamento', [p_tipo])

def sp_update_tipo_equipamento(p_id, p_tipo):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_tipo_equipamento', [p_id, p_tipo])

def sp_delete_tipo_equipamento(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_tipo_equipamento', [p_id])

def fn_read_tipo_equipamento():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_tipo_equipamento')
        return cursor.fetchall()

def fn_read_one_tipo_equipamento(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_one_tipo_equipamento', [p_id])
        return cursor.fetchall()
