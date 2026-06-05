#importaciones
import csv



#Mostrar informacion de paises
def  mostrar_paises():
    with open("datos/paises.csv", "r", encoding="utf-8") as archivo:
        lector_dic = csv.DictReader(archivo)
        
        for fila in lector_dic:
            print(f"Nombre: {fila["nombre"]} - Poblacion: {fila["poblacion"]} - Superficie: {fila["superficie"]} - Continente: {fila["continente"]} ")

