# =============================================
# INVENTARIO DE PRODUCTOS
# =============================================
# Este módulo contiene un diccionario de productos clasificados por categoría.
# Cada producto tiene: cantidad en stock, precio unitario y categoría.
# Incluye funciones para consultar, agregar y descontar productos del inventario.

inventario = {
    "Arroz Tucapel 1kg": {"cantidad": 50, "precio": 1290, "categoria": "abarrotes"},
    "Fideos Carozzi Spaghetti 500g": {"cantidad": 40, "precio": 990, "categoria": "abarrotes"},
    "Aceite Chef 900ml": {"cantidad": 30, "precio": 2990, "categoria": "abarrotes"},
    "Azúcar Iansa 1kg": {"cantidad": 45, "precio": 1390, "categoria": "abarrotes"},
    "Leche Soprole Entera 1L": {"cantidad": 35, "precio": 1190, "categoria": "lácteos"},
    "Queso Gauda Soprole 250g": {"cantidad": 25, "precio": 3490, "categoria": "lácteos"},
    "Yogurt Batido Danone 175g": {"cantidad": 60, "precio": 590, "categoria": "lácteos"},
    "Coca-Cola 1.5L": {"cantidad": 30, "precio": 1990, "categoria": "bebidas"},
    "Jugo Watt's Naranja 1L": {"cantidad": 20, "precio": 1290, "categoria": "bebidas"},
    "Agua Mineral Benedictino 1.5L": {"cantidad": 50, "precio": 890, "categoria": "bebidas"},
    "Galletas Oreo 117g": {"cantidad": 40, "precio": 1290, "categoria": "snacks"},
    "Papas Fritas Lays 90g": {"cantidad": 30, "precio": 1490, "categoria": "snacks"},
    "Maní Salado Ebner 50g": {"cantidad": 25, "precio": 690, "categoria": "snacks"},
    "Detergente Omo 1kg": {"cantidad": 20, "precio": 5990, "categoria": "limpieza"},
    "Cloro Clorox 1L": {"cantidad": 15, "precio": 1990, "categoria": "limpieza"},
    "Papel Higiénico Elite 4 rollos": {"cantidad": 40, "precio": 1990, "categoria": "limpieza"},
    "Nuggets Super Pollo 500g": {"cantidad": 18, "precio": 4990, "categoria": "congelados"},
    "Pizza Presto Pepperoni 320g": {"cantidad": 12, "precio": 3990, "categoria": "congelados"}
}

# Agrega stock a un producto existente o lo crea si no existe
def agregar_producto(nombre, cantidad, precio, categoria):
    if nombre in inventario:
        inventario[nombre]["cantidad"] += cantidad
    else:
        inventario[nombre] = {"cantidad": cantidad, "precio": precio, "categoria": categoria}

# Consulta y retorna todo el inventario
def consultar_inventario():
    return inventario

# Descuenta cantidad del inventario si hay suficiente stock
def descontar_inventario(nombre, cantidad):
    if nombre in inventario and inventario[nombre]["cantidad"] >= cantidad:
        inventario[nombre]["cantidad"] -= cantidad
        return True
    return False