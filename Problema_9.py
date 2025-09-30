pip install pyfiglet #No detecta el codigo de instalar

from pyfiglet import Figlet
import random

def imprimir_ascii():
    figlet = Figlet()

    # pedir fuente
    fuente = input("Ingrese el nombre de una fuente (o presione Enter para aleatoria): ").strip()

    if fuente == "":
        fuente = random.choice(figlet.getFonts())  # fuente aleatoria

    try:
        figlet.setFont(font=fuente)
    except:
        print("Fuente no válida. Usando aleatoria.")
        fuente = random.choice(figlet.getFonts())
        figlet.setFont(font=fuente)

    # pedir texto
    texto = input("Ingrese el texto a imprimir: ")

    # mostrar resultado
    print("\n" + figlet.renderText(texto))


# Programa principal
imprimir_ascii()