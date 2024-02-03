from .db_manager import *
from ..utils import listToJson


def create_cliente(p_email, p_senha, p_nome, p_nif):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_cliente(%s, %s, %s, %s)', [p_email, p_senha, p_nome, str(p_nif)])
        get_pg_connection().commit()

def update_cliente(p_id, p_email, p_nome, p_nif):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_cliente(%s, %s, %s, %s)', [p_id, p_email, p_nome, str(p_nif)])
        get_pg_connection().commit()

def delete_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_cliente(%s)', [p_id])
        get_pg_connection().commit()

def readone_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_cliente', [p_id])
        return listToJson(cursor.fetchone())

def readjson_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_cliente')
        return listToJson(cursor.fetchall())