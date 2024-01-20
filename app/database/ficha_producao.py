from .db_manager import *
from ..utils import listToJson

def create_ficha_producao(quantidade_equipamentos, descricao, horas, utilizador_id, tipo_mao_obra_id, equipamento_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('create_ficha_producao', [quantidade_equipamentos, descricao, horas, utilizador_id, tipo_mao_obra_id, equipamento_id])
        get_pg_connection().commit()

def update_ficha_producao(ficha_id, quantidade_equipamentos, descricao, horas, utilizador_id, tipo_mao_obra_id, equipamento_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('update_ficha_producao', [ficha_id, quantidade_equipamentos, descricao, horas, utilizador_id, tipo_mao_obra_id, equipamento_id])

def delete_ficha_producao(ficha_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_ficha_producao', [ficha_id])

def read_ficha_producao():
    with get_pg_cursor() as cursor:
        cursor.callproc('read_ficha_producao')
        return cursor.fetchall()

def readone_ficha_producao(ficha_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_ficha_producao', [ficha_id])
        return cursor.fetchone()

def readjson_ficha_producao():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_ficha_producao')
        return listToJson(cursor.fetchall())