from .db_manager import *
from ..utils import listToJson

def delete_tipo_mao_obra(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_tipo_mao_obra', [p_id])

def create_tipo_mao_obra(p_tipo, p_custo):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_tipo_mao_obra', [p_tipo, p_custo])
        get_pg_connection().commit()

def update_tipo_mao_obra(p_id, p_tipo, p_custo):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_tipo_mao_obra', [p_id, p_tipo, p_custo])

def read_tipo_mao_obra():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_tipo_mao_obra')
        return cursor.fetchall()

def readone_tipo_mao_obra(p_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_tipo_mao_obra', [p_id])
        return cursor.fetchall()

def readjson_tipo_mao_obra():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_tipo_mao_obra')
        return listToJson(cursor.fetchall())