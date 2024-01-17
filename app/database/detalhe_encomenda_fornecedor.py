from .db_manager import get_pg_cursor
from ..utils import listToJson

def delete_detalhe_encomenda_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_detalhe_encomenda_fornecedor', [p_id])

def create_detalhe_encomenda_fornecedor(p_quantidade, p_custo_entidade, p_componente_id, p_encomenda_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_detalhe_encomenda_fornecedor', [p_quantidade, p_custo_entidade, p_componente_id, p_encomenda_id])

def update_detalhe_encomenda_fornecedor(p_id, p_quantidade, p_custo_entidade, p_componente_id, p_encomenda_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_detalhe_encomenda_fornecedor', [p_id, p_quantidade, p_custo_entidade, p_componente_id, p_encomenda_id])

def read_detalhe_encomenda_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_detalhe_encomenda_fornecedor')
        return cursor.fetchall()

def readone_detalhe_encomenda_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_detalhe_encomenda_fornecedor', [p_id])
        return cursor.fetchall()

def readjson_detalhe_encomenda_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_detalhe_encomenda_fornecedor')
        return listToJson(cursor.fetchall())