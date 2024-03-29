from .db_manager import *
from ..utils import listToJson

def create_utilizador(p_email, p_senha, p_nome, p_sobrenome, p_perfil_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_utilizador(%s, %s, %s, %s, %s)', [p_email, p_senha, p_nome, p_sobrenome, int(p_perfil_id)])
        get_pg_connection().commit()

def update_utilizador(p_id, p_email, p_nome, p_sobrenome, p_perfil_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_utilizador(%s, %s, %s, %s, %s)', [p_id, p_email, p_nome, p_sobrenome, p_perfil_id])
        get_pg_connection().commit()

def delete_utilizador(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_utilizador(%s)', [p_id])
        get_pg_connection().commit()

def readone_utilizador(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_utilizador', [p_id])
        return listToJson(cursor.fetchone())

def readjson_utilizador():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_utilizador')
        return listToJson(cursor.fetchall())

def login_utilizador(email, senha):
    with get_pg_cursor() as cursor:
        cursor.execute('SELECT login_utilizador(%s, %s)', [email, senha])
        return cursor.fetchone()