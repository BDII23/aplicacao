from django.db import connections
from db_manager import get_pg_cursor

def sp_delete_encomenda_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_encomenda_cliente', [p_id])

def sp_create_encomenda_cliente(p_data_criacao, p_estado_id, p_cliente_id, p_fatura_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_encomenda_cliente', [p_data_criacao, p_estado_id, p_cliente_id, p_fatura_id])

def sp_update_encomenda_cliente(p_id, p_data_criacao, p_estado_id, p_cliente_id, p_fatura_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_encomenda_cliente', [p_id, p_data_criacao, p_estado_id, p_cliente_id, p_fatura_id])

def fn_read_encomenda_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_encomenda_cliente')
        return cursor.fetchall()

def fn_readOne_encomenda_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readOne_encomenda_cliente', [p_id])
        return cursor.fetchall()
