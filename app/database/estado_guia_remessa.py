from .db_manager import *
from ..utils import listToJson

def delete_estado_guia_remessa(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_estado_guia_remessa(%s)', [p_id])
        get_pg_connection().commit()

def create_estado_guia_remessa(p_estado):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_estado_guia_remessa(%s)', [p_estado])
        get_pg_connection().commit()
        
def update_estado_guia_remessa(p_id, p_estado):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_estado_guia_remessa(%s, %s)', [p_id, p_estado])
        get_pg_connection().commit()

def read_estado_guia_remessa():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_estado_guia_remessa')
        return cursor.fetchall()

def readone_estado_guia_remessa(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_estado_guia_remessa', [p_id])
        return listToJson(cursor.fetchone())

def readjson_estado_guia_remessa():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_estado_guia_remessa')
        return listToJson(cursor.fetchall())