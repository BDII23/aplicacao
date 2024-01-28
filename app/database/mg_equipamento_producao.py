from .db_manager import *


def read_equipamento_producao():
    collection = get_mg_collection('equipamento_producao')
    return list(collection.find())

def readone_equipamento_producao(id_equipamento):
    collection = get_mg_collection('equipamento_producao')
    return collection.find_one({"id_equipamento": id_equipamento})

def create_equipamento_producao(data):
    collection = get_mg_collection('equipamento_producao')
    result = collection.insert_one(data)
    return result.inserted_id

def update_equipamento_producao(id_equipamento, new_details):
    collection = get_mg_collection('equipamento_producao')
    result = collection.update_one(
        {"id_equipamento": id_equipamento},
        {"$set": {"detalhes": new_details}}
    )
    return result.modified_count

def delete_equipamento_producao(id_equipamento):
    collection = get_mg_collection('equipamento_producao')
    result = collection.delete_one({"id_equipamento": id_equipamento})
    return result.deleted_count
