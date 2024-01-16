from .db_manager import get_pg_cursor

def sp_delete_detalhe_encomenda_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_detalhe_encomenda_fornecedor', [p_id])

def sp_create_detalhe_encomenda_fornecedor(p_quantidade, p_custo_entidade, p_componente_id, p_encomenda_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_detalhe_encomenda_fornecedor', [p_quantidade, p_custo_entidade, p_componente_id, p_encomenda_id])

def sp_update_detalhe_encomenda_fornecedor(p_id, p_quantidade, p_custo_entidade, p_componente_id, p_encomenda_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_detalhe_encomenda_fornecedor', [p_id, p_quantidade, p_custo_entidade, p_componente_id, p_encomenda_id])

def fn_read_detalhe_encomenda_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.execute('SELECT * FROM fn_read_detalhe_encomenda_fornecedor()')
        results = cursor.fetchall()
        return results if results else ["opa"]

def fn_readone_detalhe_encomenda_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_detalhe_encomenda_fornecedor', [p_id])
        return cursor.fetchall()
