from modulos.normalizar import normalizar_texto

# Mostrar información de países
def mostrar_paises(paises):
    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    print("\n===== Países =====")

    for pais in paises:
        try:
            print(
                f"Nombre: {pais['Nombre']} | "
                f"Población: {pais['Poblacion']} | "
                f"Superficie: {pais['Superficie']} | "
                f"Continente: {pais['Continente']}"
            )
        except KeyError as e:
            print(f"Error: falta la clave {e} en un país.")

# Verificacion de paìs existente
def existe_pais(paises, nombre):
    nombre = normalizar_texto(nombre)

    for pais in paises:
        if normalizar_texto(pais["Nombre"]) == nombre:
            return True

    return False

# Agregar país
def agregar_pais(paises):

    print("\n===== Nuevo País =====")

    try:
        nombre = input("Nombre: ").strip()
        poblacion = int(input("Población: "))
        superficie = float(input("Superficie: "))
        continente = input("Continente: ").strip()

    except ValueError:
        print("\nError: Debe ingresar datos válidos.")
        return

    if nombre == "":
        print("\nError: El país debe tener un nombre.")
        return

    if existe_pais(paises, nombre):
        print("\nError: Ese país ya existe.")
        return

    if continente == "":
        print("\nError: Debe ingresar un continente.")
        return

    if poblacion < 0:
        print("\nError: La población no puede ser negativa.")
        return

    if superficie <= 0:
        print("\nError: La superficie debe ser mayor que 0.")
        return

    nuevo_pais = {
        "Nombre": nombre,
        "Poblacion": poblacion,
        "Superficie": superficie,
        "Continente": continente
    }

    paises.append(nuevo_pais)

    print("\nPaís agregado correctamente.")

# Actualizar poblacion y superficie de un pais
def actualizar_pais(paises):
    nombre_buscar = input("\nIngrese el nombre del país a actualizar: ").strip()

    if nombre_buscar == "":
        print("\nError: Debe ingresar un nombre.")
        return

    nombre_buscar_normalizado = normalizar_texto(nombre_buscar)

    for pais in paises:
        if normalizar_texto(pais["Nombre"]) == nombre_buscar_normalizado:
            print("\n===== PAÍS ENCONTRADO =====")
            print(f"Nombre: {pais['Nombre']}")
            print(f"Población actual: {pais['Poblacion']}")
            print(f"Superficie actual: {pais['Superficie']}")

            try:
                nueva_poblacion = int(input("\nIngrese la nueva población: "))
                nueva_superficie = float(input("Ingrese la nueva superficie: "))

                pais["Poblacion"] = nueva_poblacion
                pais["Superficie"] = nueva_superficie

                print("\nPaís actualizado correctamente.")
            except ValueError:
                print("\nError: Debe ingresar valores numéricos válidos.")

            return

    print("\nNo se encontró el país.")

# Buscar país
def buscar_pais(paises):

    nombre_buscar = input("\nIngrese el nombre del país a buscar: ").strip()

    nombre_buscar_normalizado = normalizar_texto(nombre_buscar)

    if nombre_buscar == "":
        print("\nError: Debe ingresar un nombre.")
        return

    encontrado = False

    for pais in paises:

        if nombre_buscar_normalizado in normalizar_texto(pais["Nombre"]):

            print("\n===== PAÍS ENCONTRADO =====")
            print(f"Nombre: {pais['Nombre']}")
            print(f"Población: {pais['Poblacion']}")
            print(f"Superficie: {pais['Superficie']}")
            print(f"Continente: {pais['Continente']}")

            encontrado = True

    if not encontrado:
        print("\nNo se encontraron países con ese nombre.")