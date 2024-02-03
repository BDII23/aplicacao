from .db_manager import *
from ..utils import listToJson

def create_estado_encomenda(p_data_criacao, p_estado):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_estado_encomenda(%s, %s)', [p_data_criacao, p_estado])
        get_pg_connection().commit()
        
def update_estado_encomenda(p_id, p_data_criacao, p_estado):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_estado_encomenda(%s, %s, %s)', [p_id, p_data_criacao, p_estado])
        get_pg_connection().commit()

def delete_estado_encomenda(p_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_estado_encomenda(%s)', [p_id])
        get_pg_connection().commit()

def readone_estado_encomenda(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_estado_encomenda', [p_id])
        return listToJson(cursor.fetchone())

def readjson_estadp_encomenda():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_estadp_encomenda')
        return listToJson(cursor.fetchall())