while True:
    try:
        fraccion = input("Ingrese una fracción (X/Y): ")
        x, y = fraccion.split("/")   # separar la fracción

        x = int(x)   # convertir a enteros
        y = int(y)

        if y == 0:
            raise ZeroDivisionError
        if x > y:
            print("Error: X no puede ser mayor que Y. Intente de nuevo.")
            continue

        porcentaje = round((x / y) * 100)

        if porcentaje <= 1:
            print("E")
        elif porcentaje >= 99:
            print("F")
        else:
            print(f"{porcentaje}%")
        break  # salir del bucle si todo salió bien

    except ValueError:
        print("Error: Debe ingresar números enteros en el formato X/Y.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0.")
