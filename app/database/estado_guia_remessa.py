from .db_manager import get_pg_cursor
from ..utils import listToJson

def delete_estado_guia_remessa(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_estado_guia_remessa', [p_id])

def create_estado_guia_remessa(p_estado):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_estado_guia_remessa', [p_estado])

def update_estado_guia_remessa(p_id, p_estado):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_estado_guia_remessa', [p_id, p_estado])

def read_estado_guia_remessa():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_estado_guia_remessa')
        return cursor.fetchall()

def readone_estado_guia_remessa(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_estado_guia_remessa', [p_id])
        return cursor.fetchall()

def readjson_estado_guia_remessa():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_estado_guia_remessa')
        return listToJson(cursor.fetchall())