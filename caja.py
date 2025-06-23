# Importamos funciones de los módulos de muestra e inventario
from muestra import descontar_muestra, consultar_muestra
from inventario import consultar_inventario

def vender_producto():
    # Pedimos al usuario el nombre del producto y la cantidad que desea comprar
    nombre = input("Ingrese el nombre del producto a vender: ").strip()
    cantidad = int(input("Ingrese la cantidad: "))

    stock_muestra = consultar_muestra()

    # Validamos si hay stock suficiente en la sala de ventas (muestra)
    if stock_muestra.get(nombre, 0) < cantidad:
        print(f"Error: Stock insuficiente en sala para '{nombre}'.")
        return False

    # Obtenemos el precio unitario del producto desde el inventario
    precio_unitario = obtener_precio_producto(nombre)
    total = precio_unitario * cantidad

    # Mostramos el total a pagar
    print(f"Total a pagar: ${total:.2f}")

    # Solicitamos al usuario que elija el método de pago
    print("\nSeleccione método de pago:")
    print("1. Efectivo")
    print("2. Tarjeta")
    opcion = input("Ingrese una opción (1 o 2): ")

    # Si elige efectivo
    if opcion == "1":
        # Pedimos el monto con el que paga
        monto_pagado = float(input("Ingrese monto con el que paga: $"))

        # Validamos si el monto es suficiente
        if monto_pagado < total:
            print("Pago insuficiente. Transacción cancelada.")
            return False

        # Calculamos el vuelto y lo mostramos
        vuelto = monto_pagado - total
        print(f"Pago exitoso. Vuelto: ${vuelto:.2f}")

    # Si elige tarjeta
    elif opcion == "2":
        print(f"Pago exitoso con tarjeta por: ${total:.2f}")

    # Si elige una opción inválida
    else:
        print("Método de pago no válido. Transacción cancelada.")
        return False

    # Descontamos la cantidad vendida desde la sala (muestra)
    descontar_muestra(nombre, cantidad)

    # Mostramos un mensaje final de éxito
    print(f"Venta registrada: {nombre} x {cantidad} = ${total:.2f}")
    return True