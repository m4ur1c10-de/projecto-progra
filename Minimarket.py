#Inventario del Minimarket
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
    "Papel Higienénico Elite 4 rollos": {"cantidad": 40, "precio": 1990, "categoria": "limpieza"},
    "Nuggets Super Pollo 500g": {"cantidad": 18, "precio": 4990, "categoria": "congelados"},
    "Pizza Presto Pepperoni 320g": {"cantidad": 12, "precio": 3990, "categoria": "congelados"}
}

entradas = []
salidas = []
caja = 0.0

#Funciona para actualizar el inventario 
def actualizar_inventario():                   #El ususario puede ingresar cuantos productos entraron y salieron
    print("\nActualización de inventario")     #Actualización de inventario
    for nombre in inventario:
        try:
            entrada = int(input(f"{nombre} - ¿Cuántos productos entraron? (0 si ninguno): "))   #Manipulación directo desde el usuario
            salida = int(input(f"{nombre} - ¿Cuántos salieron? (0 si ninguno): "))              #Manipulación directo desde el ususario
        except ValueError:
            print("Por favor ingresa solo números.")
            continue

        if entrada > 0:
            inventario[nombre]["cantidad"] += entrada
            entradas.append((nombre, entrada))

        if salida > 0:
            if salida <= inventario[nombre]["cantidad"]:
                inventario[nombre]["cantidad"] -= salida
                salidas.append((nombre, salida))
                global caja
                caja += salida * inventario[nombre]["precio"]
            else:
                print(f"⚠️ Alerta: No hay suficiente stock para descontar {salida} unidades de {nombre}.")

#Esta funcion muestra el inventario actual
def mostrar_inventario():
    print("\n--- INVENTARIO ACTUALIZADO ---")
    for nombre, datos in inventario.items():
        print(f"{nombre}: {datos['cantidad']} unidades")
        if datos['cantidad'] < 10:
            print(f"  ⚠️ Alerta: Stock bajo en {nombre} ({datos['cantidad']} unidades)")

#Aca consultamos los productos
def consultar_producto():
    while True:
        consulta = input("\n¿Quieres consultar un producto específico? (s/n): ").strip().lower()
        if consulta == "s":
            nombre = input("Escribe el nombre exacto del producto: ")
            if nombre in inventario:
                cantidad = inventario[nombre]["cantidad"]
                print(f"{nombre} tiene {cantidad} unidades disponibles.")
                if cantidad < 10:
                    print(f"  ⚠️ Alerta: Stock bajo en {nombre}.")
            else:
                print("Ese producto no existe en el inventario.")
        else:
            print("Consulta finalizada.")
            break

#A continuación se ecnuentra la función de caja
def mostrar_caja():
    print(f"\n💰 Total acumulado en caja: ${caja:.2f}")

#Gondolas le Minimarket
gondolas = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}}
categoria_a_gondola = {
    "abarrotes": 1,
    "lácteos": 2,
    "bebidas": 3,
    "snacks": 4,
    "limpieza": 5
}

def reponer_a_gondola(producto, cantidad):
    if producto in inventario:
        categoria = inventario[producto]["categoria"]
        gondola_num = categoria_a_gondola.get(categoria)

        if not gondola_num:
            print("Categoría no válida para góndolas.")
            return

        gondola = gondolas[gondola_num]
        disponible = inventario[producto]["cantidad"]
        if disponible < cantidad:
            print("⚠️ Alerta: No hay suficiente stock en inventario.")
            return

        actual_en_gondola = gondola.get(producto, {}).get("cantidad", 0)
        espacio_disponible = 30 - actual_en_gondola
        if espacio_disponible <= 0:
            print(f"⚠️ Alerta: {producto} ya está completo en góndola (30 unidades).")
            return

        cantidad_a_reponer = min(cantidad, espacio_disponible)
        inventario[producto]["cantidad"] -= cantidad_a_reponer

        if producto in gondola:
            gondola[producto]["cantidad"] += cantidad_a_reponer
        else:
            gondola[producto] = {
                "cantidad": cantidad_a_reponer,
                "precio": inventario[producto]["precio"]
            }

        print(f"Se repusieron {cantidad_a_reponer} unidades de '{producto}' en Góndola {gondola_num}.")
    else:
        print("Producto no existe en el inventario.")

def mostrar_gondolas():
    for num, productos in gondolas.items():
        print(f"\n--- Góndola {num} ---")
        if not productos:
            print("Vacía.")
        for nombre, datos in productos.items():
            print(f"{nombre}: {datos['cantidad']} unidades - ${datos['precio']}")

#Menu prinipal del sistema
def menu():
    while True:
        print("\n===== SISTEMA DE INVENTARIO - Minimarket =====")
        print("1. Actualizar inventario")
        print("2. Mostrar inventario")
        print("3. Consultar producto")
        print("4. Reponer góndola")
        print("5. Ver góndolas")
        print("6. Mostrar caja")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            actualizar_inventario()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            consultar_producto()
        elif opcion == "4":
            producto = input("Nombre exacto del producto a reponer: ")
            try:
                cantidad = int(input("Cantidad a reponer: "))
                reponer_a_gondola(producto, cantidad)
            except ValueError:
                print("Por favor ingresa una cantidad válida.")
        elif opcion == "5":
            mostrar_gondolas()
        elif opcion == "6":
            mostrar_caja()
        elif opcion == "7":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

#Inicio del sistema
menu()