<div align="center">

# Gestión de Datos de Países en Python
<br>

**Trabajo Práctico Integrador (TPI) — Programación I**
Tecnicatura Universitaria en Programación a Distancia · UTN

<br>

</div>

---

Aplicación de consola que carga un dataset de países desde un archivo CSV y ofrece
un menú interactivo para **mostrar, agregar, actualizar, buscar, filtrar, ordenar y
calcular estadísticas** sobre los datos. Desarrollada íntegramente con la biblioteca
estándar de Python (sin dependencias externas).

<br>

## Contenido

- [Características](#-características)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Cómo ejecutar](#-cómo-ejecutar)
- [Uso](#-uso)
- [Formato del CSV](#-formato-del-csv)
- [Decisiones técnicas](#-decisiones-técnicas)
- [Uso de librerías de terceros](#-uso-de-librerías-de-terceros)
- [Enlaces del proyecto](#-enlaces-del-proyecto)
- [Integrantes](#-integrantes)

<br>

---

## Características

| Funcionalidad | Descripción |
| --- | --- |
| **Carga desde CSV** | Lee el dataset con el módulo `csv.DictReader`. |
| **Mostrar** | Lista todos los países cargados. |
| **Agregar** | Da de alta un país nuevo con validación de campos. |
| **Actualizar** | Modifica la población y la superficie de un país existente. |
| **Buscar** | Por nombre, con coincidencia parcial e insensible a mayúsculas/acentos. |
| **Filtrar** | Por continente, rango de población o rango de superficie. |
| **Ordenar** | Por nombre, población o superficie, ascendente o descendente. |
| **Estadísticas** | Mayor/menor población, promedios y conteo por continente. |
| **Persistencia** | Guarda los cambios de vuelta en el archivo CSV. |

<br>

---

## Estructura del proyecto

```text
tpi-programacion/
├── main.py                 # Punto de entrada y menú principal
├── datos/
│   └── paises.csv          # Dataset base
├── modulos/
│   ├── archivos.py         # Cargar y guardar el CSV
│   ├── paises.py           # Mostrar, agregar, actualizar y buscar países
│   ├── filtros.py          # Filtros por continente, población y superficie
│   ├── ordenamientos.py    # Ordenamiento por distintos criterios
│   ├── estadisticas.py     # Cálculo y muestra de estadísticas
│   └── normalizar.py       # Normalización de texto (minúsculas y sin acentos)
└── README.md
```

Cada país se representa como un diccionario dentro de una lista global:

```python
{"Nombre": "Argentina", "Poblacion": 45376763, "Superficie": 2780400.0, "Continente": "América"}
```

<br>

---

## Cómo ejecutar

Desde la raíz del proyecto:

```bash
python main.py
```

> [!IMPORTANT]
> El programa lee `datos/paises.csv` mediante una ruta relativa, por lo que debe
> ejecutarse **desde la carpeta raíz del repositorio**.

<br>

---

##  Uso

Al iniciar se carga el CSV y se muestra el menú principal:

```text
======================
   MENU PRINCIPAL
======================
1. Mostrar todos los paises
2. Agregar pais
3. Actualizar datos del pais
4. Buscar pais
5. Filtrar pais
6. Ordenas paises
7. Mostrar estadisticas
8. Guardar cambios
9. Salir
```

Se ingresa el número de la opción deseada. Tras cada operación el sistema vuelve al
menú.

> [!NOTE]
> Para conservar los cambios realizados en memoria (altas y actualizaciones) se debe
> usar la opción **8. Guardar cambios** antes de salir.

<br>

### Ejemplos

- **Buscar** — ingresar `arg` devuelve `Argentina` (coincidencia parcial, ignora
  mayúsculas y acentos).
- **Filtrar por rango de población** — solicita un mínimo y un máximo e incluye los
  límites.
- **Ordenar** — elegir criterio (`1` Nombre, `2` Población, `3` Superficie) y
  dirección (`A` ascendente / `D` descendente).

<br>

---

## Formato del CSV

El archivo `datos/paises.csv` usa encabezado y cuatro columnas:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```

| Columna | Tipo | Notas |
| --- | --- | --- |
| `nombre` | texto | Nombre del país. |
| `poblacion` | entero | Se convierte a `int`. |
| `superficie` | decimal | Se convierte a `float` (km²). |
| `continente` | texto | Continente al que pertenece. |

<br>

---

## Decisiones técnicas

- **`Lista de diccionarios`** como estructura principal, para acceder a los datos por
  nombre de campo en lugar de por índice.
- **`csv.DictReader`** para mapear cada fila a un diccionario automáticamente.
- **`sorted()`** para ordenar sobre una copia sin alterar la lista original.
- **`try` / `except`** en las conversiones numéricas para evitar cortes ante entradas
  inválidas.
- **`Normalización de texto`** (`.lower()` + eliminación de acentos con `unicodedata`)
  para que las búsquedas y filtros sean insensibles a mayúsculas y tildes.

<br>

---

##  Uso de librerías de terceros

Este proyecto **no utiliza librerías de terceros**: funciona únicamente con la
biblioteca estándar de Python. Los módulos usados forman parte del intérprete y no
requieren instalación adicional.

| Módulo estándar | Uso en el proyecto |
| --- | --- |
| [`csv`](https://docs.python.org/3/library/csv.html) | Lectura y escritura del archivo `paises.csv`. |
| [`unicodedata`](https://docs.python.org/3/library/unicodedata.html) | Normalización de texto para quitar acentos en búsquedas y filtros. |

<br>

---

##  Enlaces del proyecto

| Recurso | Enlace |
| --- | --- |
|  **Video demostrativo** | _Completar con el enlace de YouTube_ |
| **Repositorio GitHub** | https://github.com/agussanchz/tpi-programacion.git |
<br>

---

## Integrantes

| Integrante | Comisión |
| --- | --- |
| Agustin Emiliano Sanchez| 17 |
| Maico Agustin Vivas | 5 |

---
<br>


| Profesores  ||
| --- | --- |
| Ariel Enferrel||
| Martin A. Garcia ||
| Cinthia Rigoni ||

---

<div align="center">

Proyecto académico — **Programación I** · UTN

</div>