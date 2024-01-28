from .db_manager import *
from ..utils import listToJson

def create_detalhe_encomenda_fornecedor(p_quantidade, p_custo_entidade, p_componente_id, p_encomenda_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_detalhe_encomenda_fornecedor(%s, %s, %s, %s)', [p_quantidade, p_custo_entidade, p_componente_id, p_encomenda_id])
        get_pg_connection().commit()

def update_detalhe_encomenda_fornecedor(p_id, p_quantidade, p_custo_entidade, p_componente_id, p_encomenda_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_detalhe_encomenda_fornecedor(%s, %s, %s, %s, %s)', [p_id, p_quantidade, p_custo_entidade, p_componente_id, p_encomenda_id])
        get_pg_connection().commit()

def delete_detalhe_encomenda_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_detalhe_encomenda_fornecedor(%s)', [p_id])
        get_pg_connection().commit()

def read_detalhe_encomenda_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_detalhe_encomenda_fornecedor')
        return cursor.fetchall()

def readone_detalhe_encomenda_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_detalhe_encomenda_fornecedor', [p_id])
        return listToJson(cursor.fetchone())

def readjson_detalhe_encomenda_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_detalhe_encomenda_fornecedor')
        return listToJson(cursor.fetchall())