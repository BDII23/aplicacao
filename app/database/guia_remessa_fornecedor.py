from .db_manager import *
from ..utils import listToJson

def create_guia_remessa_fornecedor(p_data_envio, p_data_entrega, p_endereco_origem, p_endereco_chegada, p_estado_id, p_detalhe_encomenda_id, p_utilizador_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_guia_remessa_fornecedor', [p_data_envio, p_data_entrega, p_endereco_origem, p_endereco_chegada, p_estado_id, p_detalhe_encomenda_id, p_utilizador_id])
        get_pg_connection().commit()

def update_guia_remessa_fornecedor(p_id, p_data_envio, p_data_entrega, p_endereco_origem, p_endereco_chegada, p_estado_id, p_detalhe_encomenda_id, p_utilizador_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_guia_remessa_fornecedor', [p_id, p_data_envio, p_data_entrega, p_endereco_origem, p_endereco_chegada, p_estado_id, p_detalhe_encomenda_id, p_utilizador_id])

def delete_guia_remessa_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_guia_remessa_fornecedor', [p_id])

def read_guia_remessa_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_guia_remessa_fornecedor')
        return cursor.fetchall()

def readone_guia_remessa_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_guia_remessa_fornecedor', [p_id])
        return cursor.fetchall()

def readjson_guia_remessa_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_guia_remessa_fornecedor')
        return listToJson(cursor.fetchall())