def mostrar_estadisticas(paises):

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    opcion = ""

    while opcion != "6":
        print("\n1. País con mayor población")
        print("2. País con menor población")
        print("3. Promedio de población")
        print("4. Promedio de superficie")
        print("5. Cantidad de países por continente")
        print("6. Salir de estadisticas")
        

        opcion = input("Opción: ")

        try:

            if opcion == "1":

                pais_mayor = paises[0]

                for pais in paises:
                    if int(pais["Poblacion"]) > int(pais_mayor["Poblacion"]):
                        pais_mayor = pais

                print(
                    f"\nPaís con mayor población: "
                    f"{pais_mayor['Nombre']} "
                    f"({pais_mayor['Poblacion']})"
                )

            elif opcion == "2":

                pais_menor = paises[0]

                for pais in paises:
                    if int(pais["Poblacion"]) < int(pais_menor["Poblacion"]):
                        pais_menor = pais

                print(
                    f"\nPaís con menor población: "
                    f"{pais_menor['Nombre']} "
                    f"({pais_menor['Poblacion']})"
                )

            elif opcion == "3":

                suma = 0

                for pais in paises:
                    suma += int(pais["Poblacion"])

                promedio = suma / len(paises)

                print(
                    f"\nPromedio de población: "
                    f"{promedio:.2f}"
                )

            elif opcion == "4":

                suma = 0

                for pais in paises:
                    suma += float(pais["Superficie"])

                promedio = suma / len(paises)

                print(
                    f"\nPromedio de superficie: "
                    f"{promedio:.2f}"
                )

            elif opcion == "5":

                continentes = {}

                for pais in paises:

                    continente = pais["Continente"]

                    if continente in continentes:
                        continentes[continente] += 1
                    else:
                        continentes[continente] = 1

                print("\nCantidad de países por continente:")

                for continente in continentes:
                    print(
                        f"{continente}: "
                        f"{continentes[continente]}"
                    )

            elif opcion == "6":
                print("\nSaliendo de menu de estadisticas...")

            else:
                print("Error: Opción inválida.")

        except ValueError:
            print("\nError: Hay datos numéricos inválidos.")

        except KeyError as e:
            print(f"\nError: Falta el campo {e}.")

