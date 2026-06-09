def ordenar_paises(paises):

    print("\n===== ORDENAR PAÍSES =====")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion = input("Opción: ")

    if opcion not in ["1", "2", "3"]:
        print('Error: Debe ingresar una opcion valida, "1", "2", "3" ')
        return

    orden = input(
        "\nA = Ascendente\n"
        "D = Descendente\n"
        "Seleccione el orden: "
    ).upper()

    if orden not in ["A", "D"]:
        print('Error: Debe colocar la letra "A" para ascendente o "D" para descendente.')
        return

    descendente = orden == "D"

    try:
        if opcion == "1":

            paises_ordenados = sorted(
                paises,
                key=lambda pais: pais["Nombre"],
                reverse=descendente
            )

        elif opcion == "2":

            paises_ordenados = sorted(
                paises,
                key=lambda pais: int(pais["Poblacion"]),
                reverse=descendente
            )

        elif opcion == "3":

            paises_ordenados = sorted(
                paises,
                key=lambda pais: float(pais["Superficie"]),
                reverse=descendente
            )

    except (ValueError, KeyError):
            print(
                "\nError: Existen datos inválidos "
                "en la lista de países."
            )
            return


    print("\n===== RESULTADO =====")

    for pais in paises_ordenados:

        print(
            f"Nombre: {pais['Nombre']} | "
            f"Población: {pais['Poblacion']} | "
            f"Superficie: {pais['Superficie']} | "
            f"Continente: {pais['Continente']}"
        )