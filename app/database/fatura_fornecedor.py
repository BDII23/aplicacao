from .db_manager import get_pg_cursor
from ..utils import listToJson

def delete_fatura_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_fatura_fornecedor', [p_id])

def create_fatura_fornecedor(p_descricao):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_fatura_fornecedor', [p_descricao])

def update_fatura_fornecedor(p_id, p_descricao):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_fatura_fornecedor', [p_id, p_descricao])

def read_fatura_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_fatura_fornecedor')
        return cursor.fetchall()

def readone_fatura_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_fatura_fornecedor', [p_id])
        return cursor.fetchall()

def readjson_fatura_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_fatura_fornecedor')
        return listToJson(cursor.fetchall())