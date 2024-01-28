from .db_manager import *
from ..utils import listToJson, getFirstElement

def delete_componente(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_componente(%s)', [p_id])
        get_pg_connection().commit()

def create_componente(p_descricao, p_quantidade, p_tipo_id, p_armazem_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_componente(%s, %s, %s, %s)', [p_descricao, p_quantidade, p_tipo_id, p_armazem_id])
        get_pg_connection().commit()

def update_componente(p_id, p_descricao, p_quantidade, p_tipo_id, p_armazem_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_componente(%s, %s, %s, %s, %s)', [p_id, p_descricao, p_quantidade, p_tipo_id, p_armazem_id])
        get_pg_connection().commit()

def read_componente():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_componente')
        return cursor.fetchall()

def readone_componente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_componente', [p_id])
        return listToJson(cursor.fetchone())

def readjson_componente():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_componente')
        return listToJson(cursor.fetchall())