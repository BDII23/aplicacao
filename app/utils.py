from datetime import datetime
import ast

def listToJson(json):
    return json[0][0]

def getFirstElement(json):
    return json[0][0][0]

def formatar_data(data_original):
    data_obj = datetime.strptime(data_original, '%Y-%m-%dT%H:%M:%S.%f')
    return data_obj.strftime('%d-%m-%Y %H:%M:%S')

def stringToArray(string):
    partes = string.strip('()').split(',')

    # Remover espaços extras e retornar a lista resultante
    return [parte.strip() for parte in partes]

def getOnlyElement(string):
	try:
		tuple_value = ast.literal_eval(string)
		if isinstance(tuple_value, tuple) and len(tuple_value) == 1:
			extracted_value = tuple_value[0]
			if isinstance(extracted_value, int):
				return extracted_value
			else:
				print("Tuple element is not an integer.")
				return ""
		else:
			print("Invalid tuple format.")
			return ""
	except (SyntaxError, ValueError) as e:
		print(f"Error: {e}")
		return ""

def getOnlyElementString(string):
	try:
		tuple_value = ast.literal_eval(string)
		if isinstance(tuple_value, tuple) and len(tuple_value) == 1:
			extracted_value = tuple_value[0]
			if isinstance(extracted_value, str):
				return extracted_value
			else:
				print("Tuple element is not an integer.")
				return ""
		else:
			print("Invalid tuple format.")
			return ""
	except (SyntaxError, ValueError) as e:
		print(f"Error: {e}")
		return ""