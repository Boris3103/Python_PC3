import requests
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    try:
        response = requests.get(url)
        response.raise_for_status()  # verificar si hubo error
        with open(nombre_archivo, "wb") as f:
            f.write(response.content)
        print(f"Imagen descargada: {nombre_archivo}")
    except requests.RequestException:
        print("Error al descargar la imagen.")


def comprimir_imagen(nombre_archivo, nombre_zip):
    with zipfile.ZipFile(nombre_zip, "w") as zipf:
        zipf.write(nombre_archivo)
    print(f"Imagen comprimida en: {nombre_zip}")


def descomprimir_zip(nombre_zip, carpeta_destino):
    with zipfile.ZipFile(nombre_zip, "r") as zipf:
        zipf.extractall(carpeta_destino)
    print(f"Archivo descomprimido en la carpeta: {carpeta_destino}")

url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=600"
nombre_imagen = "perrito.jpg"
nombre_zip = "perrito.zip"
carpeta_salida = "salida_imagen"

# Crear carpeta si no existe
os.makedirs(carpeta_salida, exist_ok=True)

descargar_imagen(url_imagen, nombre_imagen)
comprimir_imagen(nombre_imagen, nombre_zip)
descomprimir_zip(nombre_zip, carpeta_salida)