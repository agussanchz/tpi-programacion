# importaciones
import csv

# Cargar paises desde el archivo
def cargar_paises(paises):
    with open("datos/paises.csv", "r", encoding="utf-8") as archivo:
        lector_dic = csv.DictReader(archivo)
        
        for fila in lector_dic:
            pais = {
                "Nombre": fila["nombre"],
                "Poblacion": int(fila["poblacion"]),
                "Superficie": float(fila["superficie"]),
                "Continente": fila["continente"]
            }

            paises.append(pais)

