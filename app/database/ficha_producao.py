from db_manager import get_pg_cursor

def criar_ficha_producao(quantidade_equipamentos, descricao, horas, utilizador_id, tipo_mao_obra_id, equipamento_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('criar_ficha_producao', [quantidade_equipamentos, descricao, horas, utilizador_id, tipo_mao_obra_id, equipamento_id])

def atualizar_ficha_producao(ficha_id, quantidade_equipamentos, descricao, horas, utilizador_id, tipo_mao_obra_id, equipamento_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('atualizar_ficha_producao', [ficha_id, quantidade_equipamentos, descricao, horas, utilizador_id, tipo_mao_obra_id, equipamento_id])

def excluir_ficha_producao(ficha_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('excluir_ficha_producao', [ficha_id])

def obter_todas_fichas_producao():
    with get_pg_cursor() as cursor:
        cursor.callproc('obter_todas_fichas_producao')
        return cursor.fetchall()

def obter_ficha_producao_por_id(ficha_id):
    with get_pg_cursor() as cursor:
        cursor.callproc('obter_ficha_producao_por_id', [ficha_id])
        return cursor.fetchone()
