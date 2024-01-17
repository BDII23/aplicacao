from db_manager import get_pg_cursor

def sp_create_utilizador_perfil(p_perfil):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_create_utilizador_perfil', [p_perfil])

def sp_update_utilizador_perfil(p_id, p_perfil):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_update_utilizador_perfil', [p_id, p_perfil])

def sp_delete_utilizador_perfil(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('sp_delete_utilizador_perfil', [p_id])

def fn_read_utilizador_perfil():
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_read_utilizador_perfil')
        return cursor.fetchall()

def fn_readone_utilizador_perfil(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('fn_readone_utilizador_perfil', [p_id])
        return cursor.fetchall()
