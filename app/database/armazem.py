from .db_manager import *
from ..utils import listToJson

def create_armazem(p_endereco):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_armazem(%s)', [p_endereco])
        get_pg_connection().commit()

def update_armazem(p_id, p_endereco):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_armazem(%s, %s)', [p_id, p_endereco])
        get_pg_connection().commit()

def delete_armazem(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_armazem(%s)', [p_id])
        get_pg_connection().commit()

def readone_armazem(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_armazem', [p_id])
        return listToJson(cursor.fetchone())

def readjson_armazem():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_armazem')
        return listToJson(cursor.fetchall())