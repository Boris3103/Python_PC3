import requests

def obtener_tipo_cambio(year=2025):
    datos = []
    for mes in range(1, 13):  # recorrer los meses del año
        try:
            url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year={year}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # cada item tiene: fecha, compra, venta
            for d in data:
                datos.append({
                    "fecha": d["fecha"],
                    "compra": float(d["compra"]),
                    "venta": float(d["venta"])
                })

        except requests.RequestException:
            print(f"Error al obtener datos del mes {mes}")
    return datos


def analizar_tipo_cambio(datos):
    if not datos:
        print("No hay datos disponibles.")
        return

    # mínimo compra
    min_compra = min(d["compra"] for d in datos)
    fechas_min_compra = [d["fecha"] for d in datos if d["compra"] == min_compra]

    # máximo venta
    max_venta = max(d["venta"] for d in datos)
    fechas_max_venta = [d["fecha"] for d in datos if d["venta"] == max_venta]

    # diferencia máxima
    max_dif = max(d["venta"] - d["compra"] for d in datos)
    fechas_max_dif = [d["fecha"] for d in datos if (d["venta"] - d["compra"]) == max_dif]

    print("\n Análisis de tipo de cambio:")
    print(f"Compra mínima: {min_compra} en fechas: {fechas_min_compra}")
    print(f"Venta máxima: {max_venta} en fechas: {fechas_max_venta}")
    print(f"Diferencia máxima ({max_dif}): en fechas {fechas_max_dif}")


# Programa principal
datos_tc = obtener_tipo_cambio(2025)
analizar_tipo_cambio(datos_tc)