from db_manager import get_pg_cursor

def sp_create_guia_remessa_fornecedor(
    p_data_envio,
    p_data_entrega,
    p_endereco_origem,
    p_endereco_chegada,
    p_estado_id,
    p_detalhe_encomenda_id,
    p_utilizador_id
):
    with get_pg_cursor() as cursor:
        cursor.callproc(
            'sp_create_guia_remessa_fornecedor',
            [
                p_data_envio,
                p_data_entrega,
                p_endereco_origem,
                p_endereco_chegada,
                p_estado_id,
                p_detalhe_encomenda_id,
                p_utilizador_id
            ]
        )

def sp_update_guia_remessa_fornecedor(
    p_id,
    p_data_envio,
    p_data_entrega,
    p_endereco_origem,
    p_endereco_chegada,
    p_estado_id,
    p_detalhe_encomenda_id,
    p_utilizador_id
):
    with get_pg_cursor() as cursor:
        cursor.callproc(
            'sp_update_guia_remessa_fornecedor',
            [
                p_id,
                p_data_envio,
                p_data_entrega,
                p_endereco_origem,
                p_endereco_chegada,
                p_estado_id,
                p_detalhe_encomenda_id,
                p_utilizador_id
            ]
        )

def sp_delete_guia_remessa_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_guia_remessa_fornecedor', [p_id])

def fn_read_guia_remessa_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_guia_remessa_fornecedor')
        return cursor.fetchall()

def fn_readone_guia_remessa_fornecedor(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_guia_remessa_fornecedor', [p_id])
        return cursor.fetchall()
