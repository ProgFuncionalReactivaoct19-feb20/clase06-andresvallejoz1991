"""
andresvallejoz1991
"""
import csv # Importar archivos csv de excel

# Creación de las lineas del archivo
def lineasDiccionario(archivo):
	return csv.DictReader(archivo,delimiter=";")

# Apertura del archivo
with open("data/data-estudiantes.csv") as midata:
	# Impresión con la función que permita colocar los apellidos con los emails
	# Uso del split para separar el nombre del apellido y el com y no mostrarlos en pantalla
	print(list(map(lambda x: "%s-%s"%(list(x.items())[0][1].split(" ")[1], list(x.items())[1][1].split(".")[0]), lineasDiccionario(midata))))
	
	


	

