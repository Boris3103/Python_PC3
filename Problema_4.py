class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)  # heredamos de rectángulo


# Crear un rectángulo con datos del usuario
largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))
rect = Rectangulo(largo, ancho)

# Crear un cuadrado con datos del usuario
lado = float(input("Ingrese el lado del cuadrado: "))
cuad = Cuadrado(lado)

# Mostrar resultados
print("Área del rectángulo:", rect.area())
print("Área del cuadrado:", cuad.area())
