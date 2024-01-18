from .db_manager import get_pg_cursor
from ..utils import listToJson

def create_equipamento(in_descricao, in_tipo_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_equipamento', [in_descricao, in_tipo_id])

def update_equipamento(in_id, in_descricao, in_tipo_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_equipamento', [in_id, in_descricao, in_tipo_id])

def delete_equipamento(in_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_equipamento', [in_id])

def read_equipamento():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_equipamento')
        return cursor.fetchall()

def readone_equipamento(in_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_equipamento', [in_id])
        return cursor.fetchall()

def readjson_equipamento():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_equipamento')
        return listToJson(cursor.fetchall())