from .db_manager import *
from ..utils import listToJson

def create_detalhe_encomenda_cliente(_quantidade, _custo_unidade, _equipamento_id, _encomenda_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_detalhe_encomenda_cliente(%s, %s, %s, %s)', [_quantidade, _custo_unidade, _equipamento_id, _encomenda_id])
        get_pg_connection().commit()

def delete_detalhe_encomenda_cliente(_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_detalhe_encomenda_cliente(%s)', [_id])
        get_pg_connection().commit()

def update_detalhe_encomenda_cliente(_id, _quantidade, _custo_unidade, _equipamento_id, _encomenda_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_detalhe_encomenda_cliente(%s, %s, %s, %s, %s)', [_id, _quantidade, _custo_unidade, _equipamento_id, _encomenda_id])
        get_pg_connection().commit()

def readone_detalhe_encomenda_cliente(_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_detalhe_encomenda_cliente', [_id])
        return listToJson(cursor.fetchone())

def readjson_detalhe_encomenda_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_detalhe_encomenda_cliente')
        return listToJson(cursor.fetchall())