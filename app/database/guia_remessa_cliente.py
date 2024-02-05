from .db_manager import *
from ..utils import listToJson, getOnlyElementString

def delete_guia_remessa_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_guia_remessa_cliente(%s)', [p_id])
        get_pg_connection().commit()

def create_guia_remessa_cliente(p_data_envio, p_data_entrega, p_endereco_origem, p_endereco_chegada, p_utilizador_id, p_fatura_descricao, p_detalhe_encomendas):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_guia_remessa_cliente(%s, %s, %s, %s, %s, %s, %s)', [p_data_envio, p_data_entrega, p_endereco_origem, p_endereco_chegada, int(p_utilizador_id), p_fatura_descricao, list(map(int, p_detalhe_encomendas))])
        get_pg_connection().commit()

def update_guia_remessa_cliente(p_id, p_data_envio, p_data_entrega, p_endereco_origem, p_endereco_chegada, p_utilizador_id, p_fatura_descricao, p_detalhe_encomendas):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_guia_remessa_cliente(%s, %s, %s, %s, %s, %s, %s, %s)', [p_id, p_data_envio, p_data_entrega, p_endereco_origem, p_endereco_chegada, int(p_utilizador_id), p_fatura_descricao, list(map(int, p_detalhe_encomendas))])
        get_pg_connection().commit()

def readone_guia_remessa_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_guia_remessa_cliente', [p_id])
        return listToJson(cursor.fetchone())

def readjson_guia_remessa_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_guia_remessa_cliente')
        return listToJson(cursor.fetchall())
    
def readjson_guia_remessa_clientes_componentes():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_guia_remessa_clientes_componentes')
        return listToJson(cursor.fetchall())

def custo_total_guia_remessa_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('SELECT * FROM custo_total_guia_remessa_cliente(%s)', [p_id])
        get_pg_connection().commit()
        return getOnlyElementString(str(cursor.fetchone()))