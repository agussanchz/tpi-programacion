# aqui va a ir el codigo completo de nuestro sistema

# funciones para ejecutar en el menu

# menu principal

opcion = ""

while opcion != "8":

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
    print("8. Guardar y salir")

    opcion = input("\nSeleccione una opcion: ").strip()

    if opcion == "1":
        print('mostrar todos los paises que tenemos en el archivo csv')

    elif opcion == "2":
        print("Agregar pais")
    
    elif opcion == "3":
        print("Actualizar dato del pais")
    
    elif opcion == "4":
        print("Buscar pais")

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

    else:
        print('\nOpcion invalida')