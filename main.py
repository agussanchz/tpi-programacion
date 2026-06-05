# funciones para ejecutar en el menu
from modulos.archivos import cargar_paises
from modulos.paises import mostrar_paises
from modulos.paises import agregar_pais
from modulos.paises import actualizar_pais
from modulos.paises import buscar_pais

# variable global para manejar el archivo csv
paises = []

# menu principal
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
        print("   Sub menu de filtrado de paises ")
        print("======================")
        print('1. Filtrar por continente')
        print('2. Filtrar por poblacion')
        print('3. Filtrar por superficie')

    elif opcion == "6":
        print("\n======================")
        print("   Sub menu de ordenamiento de paises ")
        print("======================")
        print('1. Ordenar por nombre')
        print('2. Filtrar por poblacion')
        print('3. Filtrar por superficie (ascendente o descendente)')

    elif opcion == "7":
        print("\n======================")
        print("   Sub menu de estadisticas")
        print("======================")
        print('1. País con mayor y menor población')
        print('2. Promedio de población')
        print('3. Promedio de superficie')
        print('4. Cantidad de países por continente')

    elif opcion == "8":
        print("Guardar cambios")
    
    elif opcion == "9":
        print("Saliendo del sistema..")

    else:
        print('\nOpcion invalida')