from .db_manager import get_pg_cursor
from ..utils import listToJson

def delete_componente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_componente', [p_id])

def create_componente(p_descricao, p_quantidade, p_tipo_id, p_armazem_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_componente', [p_descricao, p_quantidade, p_tipo_id, p_armazem_id])

def update_componente(p_id, p_descricao, p_quantidade, p_tipo_id, p_armazem_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_componente', [p_id, p_descricao, p_quantidade, p_tipo_id, p_armazem_id])

def read_componente():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_componente')
        return cursor.fetchall()

def readone_componente(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_componente', [p_id])
        return cursor.fetchall()

def readjson_componente():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_componente')
        return listToJson(cursor.fetchall())