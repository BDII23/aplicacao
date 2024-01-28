from .db_manager import *
from ..utils import listToJson

def create_fornecedor(p_nome, p_nif, p_email, p_telefone, p_endereco):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_fornecedor(%s, %s, %s, %s, %s)', [p_nome, str(p_nif), p_email, str(p_telefone), p_endereco])
        get_pg_connection().commit()

def delete_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_fornecedor(%s)', [p_id])
        get_pg_connection().commit()
        
def update_fornecedor(p_id, p_nome, p_nif, p_email, p_telefone, p_endereco):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_fornecedor(%s, %s, %s, %s, %s, %s)', [p_id, p_nome, str(p_nif), p_email, str(p_telefone), p_endereco])
        get_pg_connection().commit()

def read_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_fornecedor')
        return cursor.fetchall()

def readone_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_fornecedor', [p_id])
        return listToJson(cursor.fetchone())

def readjson_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_fornecedor')
        return listToJson(cursor.fetchall())