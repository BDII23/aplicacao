from .db_manager import *
from ..utils import listToJson

def delete_detalhe_ficha_producao(detalhe_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_detalhe_ficha_producao', [detalhe_id])

def create_detalhe_ficha_producao(p_descricao, p_componente_id, p_ficha_producao_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_detalhe_ficha_producao', [p_descricao, p_componente_id, p_ficha_producao_id])
        get_pg_connection().commit()

def update_detalhe_ficha_producao(p_detalhe_id, p_descricao, p_componente_id, p_ficha_producao_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_detalhe_ficha_producao', [p_detalhe_id, p_descricao, p_componente_id, p_ficha_producao_id])

def read_detalhe_ficha_producao():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_detalhe_ficha_producao')
        return cursor.fetchall()

def readone_detalhe_ficha_producao(p_detalhe_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_detalhe_ficha_producao', [p_detalhe_id])
        return cursor.fetchall()

def readjson_detalhe_ficha_producao():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_detalhe_ficha_producao')
        return listToJson(cursor.fetchall())