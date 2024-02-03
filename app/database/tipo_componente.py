from .db_manager import *
from ..utils import listToJson

def delete_tipo_componente(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_tipo_componente(%s)', [p_id])
        get_pg_connection().commit()

def create_tipo_componente(p_tipo):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_tipo_componente(%s)', [p_tipo])
        get_pg_connection().commit()

def update_tipo_componente(p_id, p_tipo):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_tipo_componente(%s, %s)', [p_id, p_tipo])
        get_pg_connection().commit()

def readone_tipo_componente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_tipo_componente', [p_id])
        return listToJson(cursor.fetchone())

def readjson_tipo_componente():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_tipo_componente')
        return listToJson(cursor.fetchall())