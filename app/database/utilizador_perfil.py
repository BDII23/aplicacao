from .db_manager import *
from ..utils import listToJson

def create_utilizador_perfil(p_perfil):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_utilizador_perfil(%s)', [p_perfil])
        get_pg_connection().commit()

def update_utilizador_perfil(p_id, p_perfil):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_utilizador_perfil(%s, %s)', [p_id, p_perfil])
        get_pg_connection().commit()

def delete_utilizador_perfil(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_utilizador_perfil(%s)', [p_id])
        get_pg_connection().commit()

def read_utilizador_perfil():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_utilizador_perfil')
        return cursor.fetchall()

def readone_utilizador_perfil(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_utilizador_perfil', [p_id])
        return listToJson(cursor.fetchone())

def readjson_utilizador_perfil():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_utilizador_perfil')
        return listToJson(cursor.fetchall())