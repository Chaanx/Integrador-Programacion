Gestión de Países en Python
Descripción
Este proyecto es un Trabajo Práctico Integrador (TPI) de la Tecnicatura Universitaria en Programación (UTN). El objetivo es desarrollar una aplicación de consola en Python que permita gestionar información de países a partir de un archivo CSV, aplicando listas, diccionarios, funciones, condicionales, bucles, filtros, ordenamientos y estadísticas.
Requisitos técnicos
•	Python 3.10 o superior (se utiliza match/case)
•	Archivo CSV inicial con encabezados:
Código
nombre,poblacion,superficie,continente
•	Librerías estándar: csv, os
Instrucciones de uso
1.	Clonar o descargar este repositorio.
2.	Asegurarse de tener Python instalado (python --version).
3.	Ejecutar el programa desde la terminal:
bash
python main.py
4.	El sistema cargará automáticamente el archivo paises.csv (si no existe, lo crea vacío).
5.	Usar el menú interactivo para realizar operaciones.
Funcionalidades
•	Agregar país con validaciones (sin duplicados, datos obligatorios).
•	Actualizar datos de población y superficie.
•	Buscar país por nombre (coincidencia parcial o exacta).
•	Filtrar países por continente, rango de población o superficie.
•	Ordenar países por nombre, población o superficie (asc/desc).
•	Mostrar estadísticas:
o	País con mayor y menor población.
o	Promedio de población.
o	Promedio de superficie.
o	Cantidad de países por continente.
•	Mostrar catálogo completo.
•	Persistencia automática en CSV tras cada modificación.
🖥️ Ejemplo de ejecución
Código
--- MENÚ ---
1. Agregar país
2. Actualizar datos de un país
3. Buscar país por nombre
4. Filtrar por continente
5. Filtrar por rango de población
6. Filtrar por rango de superficie
7. Ordenar países
8. Mostrar estadísticas
9. Mostrar catálogo
0. Salir
Opción: 1
Nombre del país: Argentina
Población: 45376763
Superficie: 2780400
Continente: América
País agregado.
Ejemplo de estadísticas:
Código
Mayor población: {'nombre': 'Brasil', 'poblacion': 213993437, 'superficie': 8515767, 'continente': 'América'}
Menor población: {'nombre': 'Uruguay', 'poblacion': 3473727, 'superficie': 176215, 'continente': 'América'}
Promedio población: 87,345,642
Promedio superficie: 3,456,789
Cantidad por continente: {'América': 3, 'Europa': 1}
 Integrantes
•	Francisco Chanfreau
•	Juan José Diaz
 Aprendizajes
•	Uso de listas y diccionarios como estructuras principales.
•	Modularización con funciones.
•	Manejo de archivos CSV para persistencia.
•	Aplicación de filtros, ordenamientos y estadísticas.
•	Validaciones de entradas y robustez en la interacción con el usuario.

