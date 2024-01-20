from .db_manager import *
from ..utils import listToJson

def create_guia_remessa_cliente(p_data_envio, p_data_entrega, p_endereco_origem, p_endereco_chegada, p_estado_id, p_detalhe_encomenda_id, p_utilizador_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_guia_remessa_cliente', [p_data_envio, p_data_entrega, p_endereco_origem, p_endereco_chegada, p_estado_id, p_detalhe_encomenda_id, p_utilizador_id])
        get_pg_connection().commit()

def update_guia_remessa_cliente(p_id, p_data_envio, p_data_entrega, p_endereco_origem, p_endereco_chegada, p_estado_id, p_detalhe_encomenda_id, p_utilizador_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_guia_remessa_cliente', [p_id, p_data_envio, p_data_entrega, p_endereco_origem,p_endereco_chegada, p_estado_id, p_detalhe_encomenda_id, p_utilizador_id])

def delete_guia_remessa_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_guia_remessa_cliente', [p_id])

def read_guia_remessa_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_guia_remessa_cliente')
        return cursor.fetchall()

def read_one_guia_remessa_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('read_one_guia_remessa_cliente', [p_id])
        return cursor.fetchone()

def readjson_guia_remessa_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_guia_remessa_cliente')
        return listToJson(cursor.fetchall())