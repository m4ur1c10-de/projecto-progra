# =============================================
# SISTEMA DE ALERTAS
# =============================================
# Este módulo emite alertas cuando el stock en góndolas (muestrario)
# o en inventario baja de un umbral definido.
# Permite configurar umbrales mínimos por producto.

from inventario import inventario
from muestra import gondolas

# Diccionarios de umbrales mínimos por producto
umbral_inventario = {}
umbral_muestrario = {}

# Permite al usuario configurar los umbrales mínimos deseados para cada producto
def configurar_alerta(producto, tipo, umbral):
    if tipo == "inventario":
        umbral_inventario[producto] = umbral
    elif tipo == "muestrario":
        umbral_muestrario[producto] = umbral
    else:
        print("Tipo de alerta no válido. Usa 'inventario' o 'muestrario'.")

# Verifica si algún producto tiene menos stock del permitido y muestra alerta
def verificar_alertas():
    print(">>> ALERTAS DE STOCK <<<")

    # Revisar el inventario
    for producto, datos in inventario.items():
        minimo = umbral_inventario.get(producto)
        if minimo is not None and datos["cantidad"] <= minimo:
            print(f"[INVENTARIO] ALERTA: '{producto}' está bajo el mínimo ({datos['cantidad']} < {minimo})")

    # Revisar el muestrario (góndolas)
    for gondola in gondolas.values():
        for producto, datos in gondola.items():
            minimo = umbral_muestrario.get(producto)
            if minimo is not None and datos["cantidad"] <= minimo:
                print(f"[MUESTRARIO] ALERTA: '{producto}' bajo en sala de ventas ({datos['cantidad']} < {minimo})")