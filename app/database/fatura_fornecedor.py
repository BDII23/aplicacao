from .db_manager import *
from ..utils import listToJson

def delete_fatura_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_fatura_fornecedor(%s)', [p_id])
        get_pg_connection().commit()

def create_fatura_fornecedor(p_descricao):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_fatura_fornecedor(%s)', [p_descricao])
        get_pg_connection().commit()

def update_fatura_fornecedor(p_id, p_descricao):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_fatura_fornecedor(%s, %s)', [p_id, p_descricao])
        get_pg_connection().commit()

def readone_fatura_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_fatura_fornecedor', [p_id])
        return listToJson(cursor.fetchone())

def readjson_fatura_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_fatura_fornecedor')
        return listToJson(cursor.fetchall())