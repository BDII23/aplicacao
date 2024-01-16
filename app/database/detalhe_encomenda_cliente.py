from .db_manager import get_pg_cursor

def sp_delete_detalhe_encomenda_cliente(_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_detalhe_encomenda_cliente', [_id])

def sp_create_detalhe_encomenda_cliente(_quantidade, _custo_unidade, _equipamento_id, _encomenda_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_detalhe_encomenda_cliente', [_quantidade, _custo_unidade, _equipamento_id, _encomenda_id])

def sp_update_detalhe_encomenda_cliente(_id, _quantidade, _custo_unidade, _equipamento_id, _encomenda_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_detalhe_encomenda_cliente', [_id, _quantidade, _custo_unidade, _equipamento_id, _encomenda_id])

def fn_read_detalhe_encomenda_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_detalhe_encomenda_cliente')
        return cursor.fetchall()

def fn_readone_detalhe_encomenda_cliente(_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_detalhe_encomenda_cliente', [_id])
        return cursor.fetchall()
