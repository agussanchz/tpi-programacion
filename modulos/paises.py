# Mostrar informacion de paises
def mostrar_paises(paises):
    if len(paises) == 0:
        print("\nNo hay paises cargados.")
        return

    print("\n===== Paises =====")

    for pais in paises:

        print(
            f"Nombre: {pais['Nombre']} | "
            f"Poblacion: {pais['Poblacion']} | "
            f"Superficie: {pais['Superficie']} | "
            f"Continente: {pais['Continente']} "
        )

# Agregar producto
def agregar_pais(paises):

    print("\n===== Nuevo Pais =====")

    nombre = input("Nombre: ").strip()
    poblacion = int(input("Poblacion: "))
    superficie = float(input("Superficie: "))
    continente = input("Continente: ").strip()

    nuevo_pais = {
        "Nombre": nombre,
        "Poblacion": poblacion,
        "Superficie": superficie,
        "Continente": continente
    }

    paises.append(nuevo_pais)

    print("Paises agregado correctamente.")