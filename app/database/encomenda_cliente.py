from .db_manager import *
from ..utils import listToJson

def delete_encomenda_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_encomenda_cliente', [p_id])

def create_encomenda_cliente(p_data_criacao, p_estado_id, p_cliente_id, p_fatura_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_encomenda_cliente', [p_data_criacao, p_estado_id, p_cliente_id, p_fatura_id])
        get_pg_connection().commit()

def update_encomenda_cliente(p_id, p_data_criacao, p_estado_id, p_cliente_id, p_fatura_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_encomenda_cliente', [p_id, p_data_criacao, p_estado_id, p_cliente_id, p_fatura_id])

def read_encomenda_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_encomenda_cliente')
        return cursor.fetchall()

def readOne_encomenda_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_encomenda_cliente', [p_id])
        return cursor.fetchall()

def readjson_encomenda_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_encomenda_cliente')
        return listToJson(cursor.fetchall())