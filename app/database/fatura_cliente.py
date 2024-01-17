from db_manager import get_pg_cursor
from ..utils import listToJson

def delete_fatura_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_fatura_cliente', [p_id])

def create_fatura_cliente(p_descricao):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_fatura_cliente', [p_descricao])

def update_fatura_cliente(p_id, p_descricao):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_fatura_cliente', [p_id, p_descricao])

def read_fatura_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_fatura_cliente')
        return cursor.fetchall()

def readone_fatura_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_fatura_cliente', [p_id])
        return cursor.fetchall()

def readjson_fatura_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_fatura_cliente')
        return listToJson(cursor.fetchall())