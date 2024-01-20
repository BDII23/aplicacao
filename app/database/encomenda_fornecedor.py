from .db_manager import *
from ..utils import listToJson

def delete_encomenda_fornecedor(in_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_encomenda_fornecedor', [in_id])

def create_encomenda_fornecedor(in_estado_id, in_fornecedor_id, in_fatura_id=None):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_encomenda_fornecedor', [in_estado_id, in_fornecedor_id, in_fatura_id])
        get_pg_connection().commit()

def update_encomenda_fornecedor(in_id, in_estado_id, in_fornecedor_id, in_fatura_id=None):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_encomenda_fornecedor', [in_id, in_estado_id, in_fornecedor_id, in_fatura_id])

def read_encomenda_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_encomenda_fornecedor')
        return cursor.fetchall()

def readone_encomenda_fornecedor(in_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_encomenda_fornecedor', [in_id])
        return cursor.fetchall()

def readjson_encomenda_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_encomenda_fornecedor')
        return listToJson(cursor.fetchall())