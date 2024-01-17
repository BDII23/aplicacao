from db_manager import get_pg_cursor

def sp_create_utilizador(p_email, p_senha, p_nome, p_sobrenome, p_perfil_id):
    with get_pg_cursor() as cursor:
        cursor.callproc(
            'sp_create_utilizador',
            [p_email, p_senha, p_nome, p_sobrenome, p_perfil_id]
        )

def sp_update_utilizador(p_id, p_email, p_senha, p_nome, p_sobrenome, p_perfil_id):
    with get_pg_cursor() as cursor:
        cursor.callproc(
            'sp_update_utilizador',
            [p_id, p_email, p_senha, p_nome, p_sobrenome, p_perfil_id]
        )

def sp_delete_utilizador(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_utilizador', [p_id])

def fn_read_utilizador():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_utilizador')
        return cursor.fetchall()

def fn_readone_utilizador(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_utilizador', [p_id])
        return cursor.fetchall()
