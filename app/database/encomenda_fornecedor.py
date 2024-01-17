from django.db import connection
from db_manager import get_pg_cursor

def sp_delete_encomenda_fornecedor(in_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_encomenda_fornecedor', [in_id])

def sp_create_encomenda_fornecedor(in_estado_id, in_fornecedor_id, in_fatura_id=None):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_encomenda_fornecedor', [in_estado_id, in_fornecedor_id, in_fatura_id])

def sp_update_encomenda_fornecedor(in_id, in_estado_id, in_fornecedor_id, in_fatura_id=None):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_encomenda_fornecedor', [in_id, in_estado_id, in_fornecedor_id, in_fatura_id])

def fn_read_encomenda_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_encomenda_fornecedor')
        return cursor.fetchall()

def fn_readone_encomenda_fornecedor(in_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_encomenda_fornecedor', [in_id])
        return cursor.fetchall()
