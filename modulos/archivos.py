# Importaciones
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

# Guardar datos. Persistencia de archivos
def guardar_cambios(paises):
    try:

        with open("datos/paises.csv","w",newline="",encoding="utf-8") as archivo:

            escritor = csv.writer(archivo)

            escritor.writerow([
                "Nombre",
                "Poblacion",
                "Superficie",
                "Continente"
            ])

            for pais in paises:
                escritor.writerow([
                    pais["Nombre"],
                    pais["Poblacion"],
                    pais["Superficie"],
                    pais["Continente"]
                ])

        print("\nCambios guardados correctamente.")

    except Exception as e:
        print(f"\nError al guardar los cambios: {e}")