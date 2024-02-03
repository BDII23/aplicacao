from .db_manager import *
from ..utils import listToJson

def delete_encomenda_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_encomenda_cliente(%s)', [p_id])
        get_pg_connection().commit()

def create_encomenda_cliente(p_data_criacao, p_estado_id, p_cliente_id, p_fatura_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_encomenda_cliente(%s, %s, %s, %s)', [p_data_criacao, p_estado_id, p_cliente_id, p_fatura_id])
        get_pg_connection().commit()
        
def update_encomenda_cliente(p_id, p_data_criacao, p_estado_id, p_cliente_id, p_fatura_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_encomenda_cliente(%s, %s, %s, %s, %s)', [p_id, p_data_criacao, p_estado_id, p_cliente_id, p_fatura_id])
        get_pg_connection().commit()

def readone_encomenda_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_encomenda_cliente', [p_id])
        return listToJson(cursor.fetchone())

def readjson_encomenda_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_encomenda_cliente')
        return listToJson(cursor.fetchall())