from .db_manager import get_pg_cursor
from ..utils import listToJson

def create_fornecedor(p_nome, p_nif, p_email, p_telefone, p_endereco):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_fornecedor', [p_nome, p_nif, p_email, p_telefone, p_endereco])

def delete_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_fornecedor', [p_id])

def update_fornecedor(p_id, p_nome, p_nif, p_email, p_telefone, p_endereco):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_fornecedor', [p_id, p_nome, p_nif, p_email, p_telefone, p_endereco])

def read_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_fornecedor')
        return cursor.fetchall()

def readone_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_fornecedor', [p_id])
        return cursor.fetchall()

def readjson_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_fornecedor')
        return listToJson(cursor.fetchall())