"""
andresvallejoz1991
"""

import csv # Importar archivos csv de excel

#Crear las lineas del archivo
def lineas(archivo):
	return csv.reader(archivo, delimiter=";")


#Apertura del archivo
with open("data/data-estudiantes.csv") as midata:
	print(list(lineas(midata))) # Impresión de las lineas




# midata=open("data/data-estudiantes.csv") # en usos de grandes volumenes de \
		# datos es necesario para cerrar el archivo
# print(list(lineas(midata)))
# midata.close()		