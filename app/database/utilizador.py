from db_manager import get_pg_cursor
from ..utils import listToJson

def create_utilizador(p_email, p_senha, p_nome, p_sobrenome, p_perfil_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_utilizador', [p_email, p_senha, p_nome, p_sobrenome, p_perfil_id])

def update_utilizador(p_id, p_email, p_senha, p_nome, p_sobrenome, p_perfil_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_utilizador', [p_id, p_email, p_senha, p_nome, p_sobrenome, p_perfil_id])

def delete_utilizador(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_utilizador', [p_id])

def read_utilizador():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_utilizador')
        return cursor.fetchall()

def readone_utilizador(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_utilizador', [p_id])
        return cursor.fetchall()

def readjson_utilizador():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_utilizador')
        return listToJson(cursor.fetchall())