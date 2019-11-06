"""
"""
import csv # Importar archivos csv de excel

# Creación de las lineas del archivo
def lineas(archivo):
	return csv.reader(archivo, delimiter=";")

# Apertura del archivo
with open("data/data-estudiantes.csv") as midata:
	#Impresion del archivo con la función para filtrar los emails y obviar la palabra email.
	print(list(filter(lambda x: x != "email", map(lambda x: x[1], lineas(midata)))))
	
	


