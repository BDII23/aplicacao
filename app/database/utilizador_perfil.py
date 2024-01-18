from .db_manager import get_pg_cursor
from ..utils import listToJson

def create_utilizador_perfil(p_perfil):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_utilizador_perfil', [p_perfil])

def update_utilizador_perfil(p_id, p_perfil):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_utilizador_perfil', [p_id, p_perfil])

def delete_utilizador_perfil(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_utilizador_perfil', [p_id])

def read_utilizador_perfil():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_utilizador_perfil')
        return cursor.fetchall()

def readone_utilizador_perfil(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_utilizador_perfil', [p_id])
        return cursor.fetchall()

def readjson_utilizador_perfil():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_utilizador_perfil')
        return listToJson(cursor.fetchall())