# =============================================
# MUESTRA DE PRODUCTOS EN GÓNDOLAS (SALA DE VENTAS)
# =============================================
# Este módulo gestiona las góndolas por categoría.
# Permite reponer productos desde el inventario a góndolas y mostrar el estado actual.
# Incluye validaciones para verificar existencia, espacio y stock suficiente.

from inventario import inventario,consultar_inventario

# Diccionario que representa las góndolas, agrupadas por categoría
gondolas = {
    1: {},  # Góndola 1: abarrotes
    2: {},  # Góndola 2: lácteos
    3: {},  # Góndola 3: bebidas
    4: {},  # Góndola 4: snacks
    5: {}   # Góndola 5: limpieza
}

# Relación entre categoría del producto y número de góndola
categoria_a_gondola = {
    "abarrotes": 1,
    "lácteos": 2,
    "bebidas": 3,
    "snacks": 4,
    "limpieza": 5
}

# Reposición de productos desde inventario a góndolas
def reponer_a_gondola(producto, cantidad, inventario):
    # Verificamos si el producto existe en el inventario
    #for nombre, datos in inventario.items():
        #print(f"* {nombre} | Cantidad: {datos['cantidad']} | Precio: ${datos['precio']} | Categoría: {datos['categoria']}")
    if producto not in inventario:
        print("Producto no existe en el inventario. No se puede reponer.")
        return

    # Obtenemos categoría y número de góndola
    categoria = inventario[producto]["categoria"]
    gondola_num = categoria_a_gondola.get(categoria)

    # Verificamos si la categoría tiene una góndola asignada
    if gondola_num is None:
        print("Categoría no válida o sin góndola asignada.")
        return

    gondola = gondolas[gondola_num]
    disponible = inventario[producto]["cantidad"]

    # Validamos si hay suficiente stock en inventario
    if disponible < cantidad:
        print(f"No hay suficiente stock en inventario para '{producto}'. Disponible: {disponible}")
        return

    # Verificamos el espacio restante en la góndola (máximo 30 unidades por producto)
    actual_en_gondola = gondola.get(producto, {}).get("cantidad", 0)
    espacio_disponible = 30 - actual_en_gondola
    if espacio_disponible <= 0:
        print(f"{producto} ya está completo en góndola (30 unidades).")
        return

    # Calculamos cuántas unidades se pueden reponer realmente
    cantidad_a_reponer = min(cantidad, espacio_disponible)

    # Descontamos del inventario
    inventario[producto]["cantidad"] -= cantidad_a_reponer

    # Agregamos a la góndola
    if producto in gondola:
        gondola[producto]["cantidad"] += cantidad_a_reponer
    else:
        gondola[producto] = {
            "cantidad": cantidad_a_reponer,
            "precio": inventario[producto]["precio"]
        }

    print(f"Se repusieron {cantidad_a_reponer} unidades de '{producto}' en Góndola {gondola_num}.")

# Función que muestra todos los productos disponibles en todas las góndolas
def mostrar_gondolas():
    for num, productos in gondolas.items():
        print(f"\n--- Góndola {num} ---")
        if not productos:
            print("Vacía.")
        for nombre, datos in productos.items():
            print(f"{nombre}: {datos['cantidad']} unidades - ${datos['precio']}")

# Función adicional para caja: consultar todos los productos del muestrario (para validación externa)
def consultar_muestra():
    resultado = {}
    for gondola in gondolas.values():
        for producto, datos in gondola.items():
            resultado[producto] = datos["cantidad"]
    return resultado

# Función adicional para caja: descontar productos vendidos desde la góndola
def descontar_muestra(nombre, cantidad):
    for gondola in gondolas.values():
        if nombre in gondola:
            if gondola[nombre]["cantidad"] >= cantidad:
                gondola[nombre]["cantidad"] -= cantidad
                return True
            else:
                return False  # No hay suficiente stock
    return False  # Producto no existe en ninguna góndola