from django.db import connection
from db_manager import get_pg_cursor

def sp_delete_detalhe_ficha_producao(detalhe_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_detalhe_ficha_producao', [detalhe_id])

def sp_create_detalhe_ficha_producao(p_descricao, p_componente_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_detalhe_ficha_producao', [p_descricao, p_componente_id])

def sp_update_detalhe_ficha_producao(p_detalhe_id, p_descricao, p_componente_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_detalhe_ficha_producao', [p_detalhe_id, p_descricao, p_componente_id])

def fn_read_detalhe_ficha_producao():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_detalhe_ficha_producao')
        return cursor.fetchall()

def fn_readone_detalhe_ficha_producao(p_detalhe_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_detalhe_ficha_producao', [p_detalhe_id])
        return cursor.fetchall()
