"""
andresvallejoz1991
"""
import csv # Importar archivos csv de excel

# Crear todas las lineas del archivo
def lineasDiccionario(archivo):
	return csv.DictReader(archivo,delimiter="\t")

# Apertura del archivo
with open("data/trabajadores.csv") as midata:
	lista = list(lineasDiccionario(midata))
	print(list(filter(lambda x: len(list(x.items())[2][1]) >10, lista))) # Funcion que muestras los paises de más de 10 letras
	print(sorted(lista, key = lambda x: list(x.items())[1][1].split("-")[2])) # Función para ordenar en base al día de nacimiento
	
	
