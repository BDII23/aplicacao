from .db_manager import get_pg_cursor
from ..utils import listToJson

def create_estado_encomenda(p_data_criacao, p_estado):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_estado_encomenda', [p_data_criacao, p_estado])

def update_estado_encomenda(p_id, p_data_criacao, p_estado):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_estado_encomenda', [p_id, p_data_criacao, p_estado])

def delete_estado_encomenda(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_estado_encomenda', [p_id])

def read_estado_encomenda():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_estado_encomenda')
        return cursor.fetchall()

def readone_estado_encomenda(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_estado_encomenda', [p_id])
        return cursor.fetchall()

def readjson_estadp_encomenda():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_estadp_encomenda')
        return listToJson(cursor.fetchall())