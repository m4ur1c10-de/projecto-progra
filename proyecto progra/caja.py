# =============================================
# SISTEMA DE VENTAS (CAJA)
# =============================================
# Este módulo permite realizar ventas con distintos métodos de pago (efectivo o tarjeta).
# Descuenta el producto desde la sala de ventas (góndolas).
# Calcula el total a pagar y el vuelto si es necesario.
# Incluye validaciones para evitar errores al ingresar productos o cantidades inválidas.

from muestra import descontar_muestra, consultar_muestra
from inventario import consultar_inventario

def vender_producto():
    # Obtenemos el stock actual en la sala de ventas
    stock_muestra = consultar_muestra()

    # Validamos que el producto exista en la muestra y tenga stock
    while True:
        nombre = input("Ingrese el nombre del producto a vender: ").strip()
        if nombre not in stock_muestra:
            print("Producto no encontrado en la sala de ventas. Por favor, intente nuevamente.")
        else:
            if stock_muestra[nombre] == 0:
                print("El producto no tiene stock en la sala de ventas.")
            else:
                break

    # Solicitamos la cantidad deseada
    while True:
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad > stock_muestra[nombre]:
            print(f"No hay suficiente stock. Disponible: {stock_muestra[nombre]}")
        elif cantidad <= 0:
            print("Ingrese una cantidad válida mayor que 0.")
        else:
            break

    # Obtenemos el precio unitario del producto desde el inventario
    precio_unitario = obtener_precio_producto(nombre)
    total = precio_unitario * cantidad

    # Mostramos el total a pagar
    print(f"Total a pagar: ${total:.2f}")

    # Solicitamos el método de pago
    print("Seleccione método de pago:")
    print("1. Efectivo")
    print("2. Tarjeta")
    opcion = input("Ingrese una opción (1 o 2): ")

    # Pago en efectivo
    if opcion == "1":
        while True:
            try:
                monto_pagado = float(input("Ingrese monto con el que paga: $"))
                if monto_pagado < total:
                    print("Pago insuficiente. Intente nuevamente.")
                else:
                    vuelto = monto_pagado - total
                    print(f"Pago exitoso. Vuelto: ${vuelto:.2f}")
                    break
            except ValueError:
                print("Ingrese un valor numérico válido.")
    
    # Pago con tarjeta
    elif opcion == "2":
        print(f"Pago exitoso con tarjeta por: ${total:.2f}")
    
    # Opción inválida
    else:
        print("Método de pago no válido. Transacción cancelada.")
        return False

    # Descontamos el producto vendido desde la sala de ventas
    descontar_muestra(nombre, cantidad)

    # Confirmación de la venta
    print(f"Venta registrada: {nombre} x {cantidad} = ${total:.2f}")
    return True

def obtener_precio_producto(nombre):
    # Obtenemos el precio desde el inventario
    inventario = consultar_inventario()
    producto = inventario.get(nombre)
    if isinstance(producto, dict):
        return producto.get("precio", 1000)  # Precio por defecto si no existe
    return 1000