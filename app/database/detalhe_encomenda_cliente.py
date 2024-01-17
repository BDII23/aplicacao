from .db_manager import get_pg_cursor
from ..utils import listToJson

def delete_detalhe_encomenda_cliente(_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_detalhe_encomenda_cliente', [_id])

def create_detalhe_encomenda_cliente(_quantidade, _custo_unidade, _equipamento_id, _encomenda_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_detalhe_encomenda_cliente', [_quantidade, _custo_unidade, _equipamento_id, _encomenda_id])

def update_detalhe_encomenda_cliente(_id, _quantidade, _custo_unidade, _equipamento_id, _encomenda_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_detalhe_encomenda_cliente', [_id, _quantidade, _custo_unidade, _equipamento_id, _encomenda_id])

def read_detalhe_encomenda_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_detalhe_encomenda_cliente')
        return cursor.fetchall()

def readone_detalhe_encomenda_cliente(_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_detalhe_encomenda_cliente', [_id])
        return cursor.fetchall()

def readjson_detalhe_encomenda_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_detalhe_encomenda_cliente')
        return listToJson(cursor.fetchall())