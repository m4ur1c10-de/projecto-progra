# =============================================
# SISTEMA PRINCIPAL DEL MINIMARKET
# =============================================
# Este módulo actúa como el punto de entrada para el usuario.
# Permite acceder al inventario, muestrario, ventas y alertas desde un menú interactivo.
# Incluye validaciones para evitar errores al ingresar nombres o cantidades inválidas.

from inventario import agregar_producto, descontar_inventario, consultar_inventario
from muestra import reponer_a_gondola, mostrar_gondolas
from caja import vender_producto
from alertas import configurar_alerta, verificar_alertas

def menu():
    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Mostrar inventario completo")
        print("2. Agregar producto al inventario")
        print("3. Descontar producto del inventario")
        print("4. Reponer producto a góndola")
        print("5. Mostrar productos en góndolas")
        print("6. Vender producto (Caja)")
        print("7. Configurar alerta")
        print("8. Verificar alertas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario = consultar_inventario()
            print("--- Inventario ---")
            for nombre, datos in inventario.items():
                print(f"* {nombre} | Cantidad: {datos['cantidad']} | Precio: ${datos['precio']} | Categoría: {datos['categoria']}")
        
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            while True:
                try:
                    cantidad = int(input("Cantidad a agregar: "))
                    precio = int(input("Precio del producto: "))
                    break
                except ValueError:
                    print("Por favor ingrese valores numéricos válidos.")
            categoria = input("Categoría: ")
            agregar_producto(nombre, cantidad, precio, categoria)
            if agregar_producto == True:
                print(f"Producto '{nombre}' agregado o actualizado.")
        
        elif opcion == "3":
            inventario = consultar_inventario()
            while True:
                nombre = input("Nombre del producto: ")
                if nombre not in inventario:
                    print("Producto no encontrado. Por favor, intente nuevamente.")
                else:
                    break
            while True:
                try:
                    cantidad = int(input("Cantidad a descontar: "))
                    break
                except ValueError:
                    print("Por favor ingrese un número válido.")
            if descontar_inventario(nombre, cantidad):
                print(f"{cantidad} unidades de '{nombre}' descontadas del inventario.")
            else:
                print("No hay suficiente stock para descontar esa cantidad.")
        
        elif opcion == "4":
            inventario = consultar_inventario()
            while True:
                nombre = input("Nombre del producto: ")
                if nombre not in inventario:
                    print("Producto no encontrado. Por favor, intente nuevamente.")
                else:
                    break
            while True:
                try:
                    cantidad = int(input("Cantidad a reponer en góndola: "))
                    break
                except ValueError:
                    print("Por favor ingrese un número válido.")
            reponer_a_gondola(nombre, cantidad, inventario)
        
        elif opcion == "5":
            mostrar_gondolas()
        
        elif opcion == "6":
            vender_producto()
        
        elif opcion == "7":
            producto = input("Nombre del producto: ")
            tipo = input("¿Dónde desea la alerta? (inventario/muestrario): ").lower()
            while tipo not in ["inventario", "muestrario"]:
                print("Opción inválida. Escriba 'inventario' o 'muestrario'.")
                tipo = input("¿Dónde desea la alerta?: ").lower()
            while True:
                try:
                    umbral = int(input("¿Cuál es el mínimo antes de alertar?: "))
                    break
                except ValueError:
                    print("Ingrese un número válido.")
            configurar_alerta(producto, tipo, umbral)
            print("Alerta configurada.")
        
        elif opcion == "8":
            verificar_alertas()
        
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el menú principal
menu()