from .db_manager import *
from ..utils import listToJson, getOnlyElement


def create_ficha_producao(quantidade_equipamentos, descricao, horas, utilizador_id, tipo_mao_obra_id, tipo_equipamento_id, componentes):
    with get_pg_cursor() as cursor:
        cursor.execute('SELECT * FROM create_ficha_producao(%s, %s, %s, %s, %s, %s, %s)', [quantidade_equipamentos, descricao, horas, utilizador_id, int(tipo_mao_obra_id), int(tipo_equipamento_id), list(map(int, componentes))])
        get_pg_connection().commit()
        return getOnlyElement(str(cursor.fetchone()))

def update_ficha_producao(ficha_id, quantidade_equipamentos, descricao, horas, utilizador_id, tipo_mao_obra_id, tipo_equipamento_id, componentes):
    with get_pg_cursor() as cursor:
        cursor.execute('SELECT * FROM update_ficha_producao(%s, %s, %s, %s, %s, %s, %s, %s)', [ficha_id, quantidade_equipamentos, descricao, horas, utilizador_id, int(tipo_mao_obra_id), int(tipo_equipamento_id), list(map(int, componentes))])
        get_pg_connection().commit()
        return getOnlyElement(str(cursor.fetchone()))

def delete_ficha_producao(ficha_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('delete_ficha_producao', [ficha_id])

def readone_ficha_producao(_ficha_producao_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('readone_ficha_producao', [_ficha_producao_id])
        return listToJson(cursor.fetchone())

def readjson_ficha_producao():
    with get_pg_cursor() as cursor:
        cursor.callproc('readjson_ficha_producao')
        return listToJson(cursor.fetchall())