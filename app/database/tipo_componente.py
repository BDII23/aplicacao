from .db_manager import *
from ..utils import listToJson

def create_tipo_componente(p_tipo):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_tipo_componente', [p_tipo])
        get_pg_connection().commit()

def delete_tipo_componente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_tipo_componente', [p_id])

def update_tipo_componente(p_id, p_tipo):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_tipo_componente', [p_id, p_tipo])

def read_tipo_componente():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_tipo_componente')
        return cursor.fetchall()

def readone_tipo_componente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_tipo_componente', [p_id])
        return cursor.fetchall()

def readjson_tipo_componente():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_tipo_componente')
        return listToJson(cursor.fetchall())