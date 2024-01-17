from db_manager import get_pg_cursor

def sp_delete_fatura_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_fatura_cliente', [p_id])

def sp_create_fatura_cliente(p_descricao):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_fatura_cliente', [p_descricao])

def sp_update_fatura_cliente(p_id, p_descricao):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_fatura_cliente', [p_id, p_descricao])

def fn_read_fatura_cliente():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_fatura_cliente')
        return cursor.fetchall()

def fn_readone_fatura_cliente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_fatura_cliente', [p_id])
        return cursor.fetchall()
