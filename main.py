# Funciones para ejecutar en el menu
from modulos.archivos import cargar_paises
from modulos.paises import mostrar_paises
from modulos.paises import agregar_pais
from modulos.paises import actualizar_pais
from modulos.paises import buscar_pais
from modulos.filtros import filtrar_paises
from modulos.ordenamientos import ordenar_paises
from modulos.estadisticas import mostrar_estadisticas
from modulos.archivos import guardar_cambios

# Variable global para manejar el archivo csv
paises = []

# Menu principal
cargar_paises(paises)
opcion = ""

while opcion != "9":

    print("\n======================")
    print("   MENU PRINCIPAL")
    print("======================")
    print("1. Mostrar todos los paises")
    print("2. Agregar pais")
    print("3. Actualizar datos del pais")
    print("4. Buscar pais")
    print("5. Filtrar pais")
    print("6. Ordenas paises")
    print("7. Mostrar estadisticas")
    print("8. Guardar cambios")
    print("9. Salir")

    opcion = input("\nSeleccione una opcion: ").strip()

    if opcion == "1":
        mostrar_paises(paises)

    elif opcion == "2":
        agregar_pais(paises)
    
    elif opcion == "3":
        actualizar_pais(paises)
    
    elif opcion == "4":
        buscar_pais(paises)

    elif opcion == "5":
        print("\n======================")
        print("  Filtrado de paises ")
        print("======================")
        filtrar_paises(paises)

    elif opcion == "6":
        print("\n======================")
        print("Ordenamiento de paises ")
        print("======================")
        ordenar_paises(paises)

    elif opcion == "7":
        print("\n======================")
        print("    Estadisticas   ")
        print("======================")
        mostrar_estadisticas(paises)

    elif opcion == "8":
        guardar_cambios(paises)
    
    elif opcion == "9":
        print("Saliendo del sistema..")

    else:
        print('\nOpcion invalida')