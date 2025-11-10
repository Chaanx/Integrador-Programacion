import csv
import os


def cargar_datos(ruta_archivo):
    lista_paises = []

    if not os.path.exists(ruta_archivo):
        print(f"El archivo '{ruta_archivo}' no se encontró.")
        return []
    
    with open(ruta_archivo, mode='r', encoding='utf-8', newline='') as archivo:
        lector_csv = csv.DictReader(archivo)

        for fila in lector_csv:
            lista_paises.append({
                "nombre": fila["nombre"],
                "poblacion": int(fila["poblacion"]),
                "superficie": int(fila["superficie"]),
                "continente": fila["continente"],
            })
    return lista_paises

def guardar_datos(lista_paises, ruta_archivo):
    if not lista_paises:
        print("No hay datos para guardar")
        return
    
    with open(ruta_archivo, mode='w', encoding='utf-8', newline='') as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=['nombre', 'poblacion', 'superficie', 'continente'])
        escritor_csv.writeheader()
        escritor_csv.writerows(lista_paises)

def validar_entero_positivo(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        else:
            print("Error: Debe ingresar un número entero positivo")

def validar_cadena_no_vacia(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.strip():
            return entrada
        else:
            print("Error: El campo no puede estar vacío")

def mostrar_lista_paises(lista_paises):
    if not lista_paises:
        print("No se encontraron coincidencias")
        return
    
    print("\n--- Resultados ---\n")
    print(f"{'Nombre':<25} | {'Continente':<15} | {'Población':>15} | {'Superficie (km2)':>20}")
    print("-" * 80)

    for pais in lista_paises:
        nombre = pais['nombre']
        continente = pais['continente']
        poblacion = pais['poblacion']
        superficie = pais['superficie']
        print(f"{nombre:<25} | {continente:<15} | {poblacion:>15,} | {superficie:>20,}")

def filtrar_paises(lista_paises):
    if not lista_paises:
        print("No hay países para filtrar")
        return
    
    print("\n--- Menú de Filtros ---")
    print("1. Filtrar por Continente")
    print("2. Filtrar por Rango de Población")
    print("3. Filtrar por Rango de Superficie")
    opcion = input("Seleccione una opción: ")

    resultados = []

    match opcion:
        case "1":
            continente_buscado = validar_cadena_no_vacia("Ingrese el nombre del continente: ")
            for pais in lista_paises:
                if pais['continente'].lower() == continente_buscado.lower():
                    resultados.append(pais)
            print(f"\nPaíses en '{continente_buscado}':")
            mostrar_lista_paises(resultados)
         
        case "2":
            print("Ingrese el rango de población")
            poblacion_min = validar_entero_positivo("Población mínima: ")
            poblacion_max = validar_entero_positivo("Población máxima: ")

            if poblacion_min > poblacion_max:
                print("Error: La población mínima no puede ser mayor que la máxima")
                return
            
            for pais in lista_paises:
                if poblacion_min <= pais['poblacion'] <= poblacion_max:
                    resultados.append(pais)
            print(f"\nPaíses con población entre {poblacion_min:,} y {poblacion_max:,}:")
            mostrar_lista_paises(resultados)

        case "3":
            print("Ingrese el rango de superficie (en km2)")
            superficie_min = validar_entero_positivo("Superficie mínima: ")
            superficie_max = validar_entero_positivo("Superficie máxima: ")

            if superficie_min > superficie_max:
                print("Error: La superficie mínima no puede ser mayor que la máxima")
                return
            
            for pais in lista_paises:
                if superficie_min <= pais['superficie'] <= superficie_max:
                    resultados.append(pais)
            print(f"\nPaíses con superficie entre {superficie_min:,} y {superficie_max:,}:")
            mostrar_lista_paises(resultados)

        case _:
            print("Opción no válida")

def buscar_pais(lista_paises):
    if not lista_paises:
        print("No hay países en la lista para buscar")
        return
    
    termino_a_buscar = validar_cadena_no_vacia("Ingrese nombre o parte del país a buscar: ")

    resultados = []

    for pais in lista_paises:
        if termino_a_buscar.lower() in pais['nombre'].lower():
            resultados.append(pais)

    if resultados:
        print(f"\nPaíses encontrados que incluyen '{termino_a_buscar}': ")
        mostrar_lista_paises(resultados)
    else:
        print(f"No se encontraron países que coincidan con '{termino_a_buscar}'")

def obtener_nombre(pais):
    return pais['nombre']

def obtener_poblacion(pais):
    return pais['poblacion']

def obtener_superficie(pais):
    return pais['superficie']

def ordenar_paises(lista_paises):
    if not lista_paises:
        print("No hay países para ordenar")
        return
    
    print("Seleccione el criterio de ordenamiento:")
    print("1. Por Nombre")
    print("2. Por Población")
    print("3. Por Superficie")
    opcion = input("Opción: ")

    orden_ascendente = input("¿Orden ascendente (S/N)? ").strip().upper()
    es_decendente = (orden_ascendente != 'S')

    lista_ordenada = []

    match opcion:
        case "1":
            lista_ordenada = sorted(lista_paises, key=obtener_nombre, reverse=es_decendente)

        case "2":
            lista_ordenada = sorted(lista_paises, key=obtener_poblacion, reverse=es_decendente)

        case "3":
            lista_ordenada = sorted(lista_paises, key=obtener_superficie, reverse=es_decendente)

        case _:
            print("Opción no válida")

    print("\n--- Lista de Países Ordenada ---")
    if not lista_ordenada:
        print("No se pudo ordenar la lista")
    else:
        mostrar_lista_paises(lista_ordenada)

def agregar_pais(lista_paises):
    print("Ingrese los datos del nuevo país: ")

    nombre = validar_cadena_no_vacia("Nombre: ")
    poblacion = validar_entero_positivo("Población: ")
    superficie = validar_entero_positivo("Superficie (km2): ")
    continente = validar_cadena_no_vacia("Continente: ")

    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente,
    }

    lista_paises.append(nuevo_pais)
    print(f"{nombre} fue agregado")

def actualizar_pais(lista_paises):
    if not lista_paises:
        print("No hay países en la lista para actualizar")
        return
    
    nombre_a_buscar = validar_cadena_no_vacia("Ingrese el nombre del país que quiere actualizar: ")

    pais_encontrado = None

    for pais in lista_paises:
        if pais['nombre'].lower() == nombre_a_buscar.lower():
            pais_encontrado = pais
            break

    if pais_encontrado:
        print(f"País encontrado: {pais_encontrado['nombre']}")
        print(f"Población actual: {pais_encontrado['poblacion']}")
        print(f"Superficie actual: {pais_encontrado['superficie']} km2")

        nueva_poblacion = validar_entero_positivo("Ingrese la nueva población: ")
        nueva_superficie = validar_entero_positivo("Ingrese la nueva superficie (km2): ")

        pais_encontrado['poblacion'] = nueva_poblacion
        pais_encontrado['superficie'] = nueva_superficie

        print(f"Datos de '{pais_encontrado['nombre']}' actualizados")
    else:
        print(f"Error: No se encontró '{nombre_a_buscar}'")

def mostrar_estadisticas(lista_paises):
    if not lista_paises:
        print("No hay países cargados para calcular estadísticas.")
        return

    mayor = max(lista_paises, key=obtener_poblacion)
    menor = min(lista_paises, key=obtener_poblacion)
    promedio_poblacion = sum(p['poblacion'] for p in lista_paises) / len(lista_paises)
    promedio_superficie = sum(p['superficie'] for p in lista_paises) / len(lista_paises)

    conteo_continentes = {}
    for pais in lista_paises:
        cont = pais['continente']
        conteo_continentes[cont] = conteo_continentes.get(cont, 0) + 1

    print("\n--- Estadísticas ---")
    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']:,})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']:,})")
    print(f"Promedio de población: {promedio_poblacion:,.2f}")
    print(f"Promedio de superficie: {promedio_superficie:,.2f} km²")
    print("Cantidad de países por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"  {continente}: {cantidad}")


def mostrar_menu():
    print("\n" + "=" * 40)
    print("--- GESTIÓN DE DATOS DE PAÍSES ---")
    print("=" * 40)
    print("1. Agregar un país")
    print("2. Actualizar datos de un país")
    print("3. Buscar un país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir (y guardar datos)")
    print("=" * 40)


def main():
    lista_paises = cargar_datos('paises.csv')

    if not lista_paises:
        print("No se pudieron cargar datos. Se iniciará con una lista vacía")
        lista_paises = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                print("\n== 1. Agregar un país ==")
                agregar_pais(lista_paises)
            case "2":
                print("\n== 2. Actualizar datos de un país ==")
                actualizar_pais(lista_paises)
            case "3":
                print("\n== 3. Buscar un país por nombre ==")
                buscar_pais(lista_paises)
            case "4":
                print("\n== 4. Filtrar países ==")
                filtrar_paises(lista_paises)
            case "5":
                print("\n== 5. Ordenar países ==")
                ordenar_paises(lista_paises)
            case "6":
                print("\n== 6. Mostrar estadísticas==")
                mostrar_estadisticas(lista_paises)
            case "7":
                print("\n== 7. Salir (y guardar datos) ==")
                guardar_datos(lista_paises, 'paises.csv')
                
                break
            case _:
                print("Error: Ingrese un número de 1-7")

main()