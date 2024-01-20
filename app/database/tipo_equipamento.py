from .db_manager import *
from ..utils import listToJson

def create_tipo_equipamento(p_tipo):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_tipo_equipamento', [p_tipo])
        get_pg_connection().commit()

def update_tipo_equipamento(p_id, p_tipo):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_tipo_equipamento', [p_id, p_tipo])

def delete_tipo_equipamento(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_tipo_equipamento', [p_id])

def read_tipo_equipamento():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_tipo_equipamento')
        return cursor.fetchall()

def readone_tipo_equipamento(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_tipo_equipamento', [p_id])
        return cursor.fetchall()

def readjson_tipo_equipamento():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_tipo_equipamento')
        return listToJson(cursor.fetchall())