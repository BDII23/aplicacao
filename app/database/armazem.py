from .db_manager import *
from ..utils import listToJson

def create_armazem(p_endereco):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_armazem', [p_endereco])
        get_pg_connection().commit()

def update_armazem(p_id, p_endereco):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_armazem', [p_id, p_endereco])

def delete_armazem(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_armazem', [p_id])

def read_armazem():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_armazem')
        return cursor.fetchall()

def readone_armazem(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_armazem', [p_id])
        return cursor.fetchall()

def readjson_armazem():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_armazem')
        return listToJson(cursor.fetchall())