"""
andresvallejoz1991
"""

import csv # Importar archivos csv de excel
# def lineas(archivo):
	# return csv.reader(archivo,delimiter=";")

# Creación de las lineas del archivo
def lineasDiccionario(archivo):
	return csv.DictReader(archivo,delimiter=";")

# Apertura del archivo
with open("data/data-estudiantes.csv") as midata:
	# Impresión con la función para mostras las posición [0][1] del archivo
	print(list(map(lambda x: list(x.items())[0][1],lineasDiccionario(midata))))
	# print(list(lineasDiccionario(midata)))

