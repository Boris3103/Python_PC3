# Problema 3: Cargar listado de alumnos
def cargar_alumnos():
    alumnos = []
    n = int(input("¿Cuántos alumnos desea ingresar?: "))

    for i in range(n):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        notas = []

        for j in range(3):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {j+1} de {nombre} (0-10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("Error: ingrese solo números.")

        alumno = {"Nombre": nombre, "Notas": notas}
        alumnos.append(alumno)

    return alumnos


# Problema 5: evaluar aprobados y desaprobados
def evaluar_aprobados(alumnos):
    aprobados = 0
    desaprobados = 0

    for alumno in alumnos:
        promedio = sum(alumno["Notas"]) / len(alumno["Notas"])
        alumno["Promedio"] = promedio  # guardamos promedio en el diccionario

        if promedio >= 4:
            aprobados += 1
        else:
            desaprobados += 1

    print("\n Resultados de aprobación:")
    print("Aprobados:", aprobados)
    print("Desaprobados:", desaprobados)


# Problema 6: promedio general del curso
def promedio_curso(alumnos):
    suma_total = 0
    cantidad_notas = 0

    for alumno in alumnos:
        suma_total += sum(alumno["Notas"])
        cantidad_notas += len(alumno["Notas"])

    promedio = suma_total / cantidad_notas if cantidad_notas > 0 else 0
    print("\n Promedio general del curso:", round(promedio, 2))


# Problema 7: mejor y peor promedio
def mejor_y_peor_promedio(alumnos):
    if not alumnos:
        print("No hay alumnos registrados.")
        return

    mejor = max(alumnos, key=lambda a: a["Promedio"])
    peor = min(alumnos, key=lambda a: a["Promedio"])

    print("\n Alumno con el promedio más alto:")
    print(f"{mejor['Nombre']} → {mejor['Promedio']:.2f}")

    print("\n Alumno con el promedio más bajo:")
    print(f"{peor['Nombre']} → {peor['Promedio']:.2f}")


# Otro problema 7: buscar alumno por nombre (parcial o completo)
def buscar_alumno(alumnos, nombre_buscar):
    encontrados = []
    for alumno in alumnos:
        if nombre_buscar.lower() in alumno["Nombre"].lower():
            encontrados.append(alumno)

    if encontrados:
        print("\n Resultados de la búsqueda:")
        for alumno in encontrados:
            print(f"Alumno: {alumno['Nombre']}, Notas: {alumno['Notas']}, Promedio: {alumno['Promedio']:.2f}")
    else:
        print("\n No se encontraron alumnos con ese nombre.")


alumnos = cargar_alumnos()
evaluar_aprobados(alumnos)
promedio_curso(alumnos)
mejor_y_peor_promedio(alumnos)

# Buscar alumno
nombre = input("\nIngrese un nombre o parte de un nombre para buscar: ")
buscar_alumno(alumnos, nombre)