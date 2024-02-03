from .db_manager import *
from ..utils import listToJson, getOnlyElement

def create_equipamento(in_tipo_id):
    with get_pg_cursor() as cursor:
        cursor.execute('SELECT * FROM create_equipamento(%s)', [in_tipo_id])
        get_pg_connection().commit()
        return getOnlyElement(str(cursor.fetchone()))

def update_equipamento(in_id, in_tipo_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_equipamento(%s, %s)', [in_id, in_tipo_id])
        get_pg_connection().commit()

def delete_equipamento(in_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_equipamento(%s)', [in_id])
        get_pg_connection().commit()

def readone_equipamento(in_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_equipamento', [in_id])
        return listToJson(cursor.fetchone())

def readjson_equipamento():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_equipamento')
        return listToJson(cursor.fetchall())