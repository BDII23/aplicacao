from .db_manager import *


def read_equipamento_producao():
    collection = get_mg_collection('equipamento_producao')
    return list(collection.find())

def readone_equipamento_producao(equipamento_id):
    collection = get_mg_collection('equipamento_producao')
    return collection.find_one({"equipamento_id": equipamento_id})

def create_equipamento_producao(equipamento_id, atributo):
    collection = get_mg_collection('equipamento_producao')
    print("opa1")
    documento = { "equipamento_id": equipamento_id, "atributo": atributo }
    print("opa2")
    
    result = collection.insert_one(documento)
    print("opa3")
    return result.inserted_id

def update_equipamento_producao(equipamento_id, atributo):
    collection = get_mg_collection('equipamento_producao')
    result = collection.update_one(
        {"equipamento_id": equipamento_id},
        {"$set": {"atributo": atributo}}
    )
    return result.modified_count

def delete_equipamento_producao(equipamento_id):
    collection = get_mg_collection('equipamento_producao')
    result = collection.delete_one({"equipamento_id": equipamento_id})
    return result.deleted_count
