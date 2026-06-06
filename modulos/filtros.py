from modulos.normalizar import normalizar_texto

# Funcion de filtros de paises
def filtrar_paises(paises):

    opcion = input(
        "\n1. Continente\n"
        "2. Rango de población\n"
        "3. Rango de superficie\n"
        "Opción: "
    )

    #Filtro de continente
    if opcion == "1":

        continente = input("\nIngrese el continente: ").strip()

        if continente == "":
            print("Error: Debe ingresar un continente.")
            return

        encontrado = False

        continente_normalizado = normalizar_texto(continente)

        for pais in paises:

            if normalizar_texto(pais["Continente"]) == continente_normalizado:

                print(
                    f"{pais['Nombre']} | "
                    f"{pais['Poblacion']} | "
                    f"{pais['Superficie']}"
                )

                encontrado = True

        if not encontrado:
            print(
                "\nNo se encontraron países "
                "para ese continente."
            )

    #Filtro de Poblacion
    elif opcion == "2":

        try:
            minimo = int(input("Población mínima: "))
            maximo = int(input("Población máxima: "))

            if minimo < 0 or maximo < 0:
                print("Error: La población no puede ser negativa.")
                return

            if minimo > maximo:
                print("Error: El mínimo no puede ser mayor que el máximo.")
                return

            encontrado = False

            for pais in paises:

                if minimo <= int(pais["Poblacion"]) <= maximo:

                    print(
                        f"\n{pais['Nombre']} | "
                        f"{pais['Poblacion']} habitantes"
                    )

                    encontrado = True

            if not encontrado:
                print(
                    "\nNo se encontraron países "
                    "dentro de ese rango de población."
                )

        except ValueError:
            print("Error: Ingrese datos válidos.")

    #Filtro de superfice
    elif opcion == "3":

        try:
            minimo = float(input("Superficie mínima: "))
            maximo = float(input("Superficie máxima: "))

            if minimo < 0 or maximo < 0:
                print("Error: La superficie no puede ser negativa.")
                return

            if minimo > maximo:
                print("Error: El mínimo no puede ser mayor que el máximo.")
                return

            encontrado = False

            for pais in paises:

                if minimo <= float(pais["Superficie"]) <= maximo:

                    print(
                        f"\n{pais['Nombre']} | "
                        f"{pais['Superficie']} km²"
                    )

                    encontrado = True

            if not encontrado:
                print(
                    "\nNo se encontraron países "
                    "dentro de ese rango de superficie."
                )

        except ValueError:
            print("Error: Ingrese datos válidos.")

    else:
        print("Opción inválida.")