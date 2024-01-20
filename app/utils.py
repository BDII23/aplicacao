from datetime import datetime

def listToJson(json):
    return json[0][0]

def getFirstElement(json):
    return json[0][0][0]

def formatar_data(data_original):
    data_obj = datetime.strptime(data_original, '%Y-%m-%dT%H:%M:%S.%f')
    return data_obj.strftime('%d-%m-%Y %H:%M:%S')