from .db_manager import *
from ..utils import listToJson

def delete_encomenda_fornecedor(in_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL delete_encomenda_fornecedor(%s)', [in_id])
        get_pg_connection().commit()

def create_encomenda_fornecedor(in_componentes, in_fornecedor_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL create_encomenda_fornecedor(%s, %s)', [list(map(int, in_componentes)), int(in_fornecedor_id)])
        get_pg_connection().commit()

def importar_encomenda_fornecedor(in_json):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL importar_encomenda_fornecedor(%s)', [in_json])
        get_pg_connection().commit()

def exportar_encomenda_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('exportar_encomenda_fornecedor')
        return listToJson(cursor.fetchall())
        
def update_encomenda_fornecedor(in_id, in_componentes, in_fornecedor_id):
    with get_pg_cursor() as cursor:
        cursor.execute('CALL update_encomenda_fornecedor(%s, %s, %s)', [in_id, list(map(int, in_componentes)), int(in_fornecedor_id)])
        get_pg_connection().commit()

def readone_encomenda_fornecedor(in_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_encomenda_fornecedor', [in_id])
        return listToJson(cursor.fetchone())

def readjson_encomenda_fornecedor():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_encomenda_fornecedor')
        return listToJson(cursor.fetchall())