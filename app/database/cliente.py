from .db_manager import get_pg_cursor
from ..utils import listToJson

def create_cliente(p_email, p_senha, p_nome, p_nif):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_cliente', [p_email, p_senha, p_nome, p_nif])

def update_cliente(p_id, p_email, p_senha, p_nome, p_nif):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_cliente', [p_id, p_email, p_senha, p_nome, p_nif])

def delete_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_cliente', [p_id])

def read_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_cliente')
        return cursor.fetchall()

def readone_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_cliente', [p_id])
        return cursor.fetchone()

def readjson_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_cliente')
        return listToJson(cursor.fetchall())