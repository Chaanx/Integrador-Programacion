# Gestión de Países en Python

## Descripción

Este proyecto es un Trabajo Práctico Integrador (TPI) de la Tecnicatura Universitaria en Programación (UTN). El objetivo es desarrollar una aplicación de consola en Python que permita gestionar información de países a partir de un archivo CSV, aplicando listas, diccionarios, funciones, condicionales, bucles, filtros, ordenamientos y estadísticas.

## Requisitos técnicos

  * Python 3.10 o superior (se utiliza `match/case`)
  * Archivo CSV inicial con encabezados:
    ```csv
    nombre,poblacion,superficie,continente
    ```
  * Librerías estándar: `csv`, `os`

## Instrucciones de uso

1.  Clonar o descargar este repositorio.
2.  Asegurarse de tener Python instalado (`python --version`).
3.  Ejecutar el programa desde la terminal:
    ```bash
    python main.py
    ```
4.  El sistema cargará automáticamente el archivo `paises.csv` (si no existe, lo crea vacío).
5.  Usar el menú interactivo para realizar operaciones.

## Funcionalidades

  * Agregar país con validaciones (sin duplicados, datos obligatorios).
  * Actualizar datos de población y superficie.
  * Buscar país por nombre (coincidencia parcial o exacta).
  * Filtrar países por continente, rango de población o superficie.
  * Ordenar países por nombre, población o superficie (asc/desc).
  * Mostrar estadísticas:
      * País con mayor y menor población.
      * Promedio de población.
      * Promedio de superficie.
      * Cantidad de países por continente.
  * Mostrar catálogo completo.
  * Persistencia automática en CSV tras cada modificación.

## 🖥️ Ejemplo de ejecución

```text
== 7. Listar todos los países ==

--- Resultados ---

Nombre                    | Continente      |       Población |     Superficie (km2)
--------------------------------------------------------------------------------
Argentina                 | América         |      45,376,763 |            2,780,400
Japón                     | Asia            |     125,800,000 |              377,975
Brasil                    | América         |     213,993,437 |            8,515,767
Alemania                  | Europa          |      83,149,300 |              357,022

========================================
--- GESTIÓN DE DATOS DE PAÍSES ---
========================================
1. Agregar un país
2. Actualizar datos de un país
3. Buscar un país por nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Listar todos los países
8. Salir (y guardar datos)
========================================
Seleccione una opción: 
```

Ejemplo de estadísticas:

```text
========================================
--- Estadísticas ---
========================================
País con mayor población: Brasil (213,993,437)
País con menor población: Argentina (45,376,763)
Promedio de población: 117,079,875.00
Promedio de superficie: 3,007,791.00 km²
========================================
Cantidad de países por continente:
========================================
  América: 2
  Asia: 1
  Europa: 1

========================================
--- GESTIÓN DE DATOS DE PAÍSES ---
========================================
1. Agregar un país
2. Actualizar datos de un país
3. Buscar un país por nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Listar todos los países
8. Salir (y guardar datos)
========================================
Seleccione una opción: 
```

## Integrantes

  * Francisco Chanfreau
  * Juan José Diaz

## Aprendizajes

  * Uso de listas y diccionarios como estructuras principales.
  * Modularización con funciones.
  * Manejo de archivos CSV para persistencia.
  * Aplicación de filtros, ordenamientos y estadísticas.
  * Validaciones de entradas y robustez en la interacción con el usuario.

