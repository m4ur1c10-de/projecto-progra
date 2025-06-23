#Caso 1 de fundamentos de programación, jornada miercoles
#Caso aplicado con procentajes bajo el 100% con 4 notas

Nota_1= float (input("Ingrese nota 1: "))

if Nota_1 <1.0:
    print("Fuera de rango, vuela a ingresar la nota 1")
if Nota_1 >7.0:
    print("Fuera de rango, vuelva a ingresar nota 1")

Nota_2= float (input("Ingrese nota 2: "))

if Nota_2 <1.0:
    print("Fuera de rango, vuela a ingresar la nota 2")
if Nota_2 >7.0:
    print("Fuera de rango, vuelva a ingresar nota 2")

Nota_3= float (input("Ingrese nota 3: "))

if Nota_3 <1.0:
    print("Fuera de rango, vuela a ingresar la nota 3")
if Nota_3 >7.0:
    print("Fuera de rango, vuelva a ingresar nota 3")

Nota_4= float (input("Ingrese nota 4: "))

if Nota_4 <1.0:
    print("Fuera de rango, vuela a ingresar la nota 4")
if Nota_4 >7.0:
    print("Fuera de rango, vuelva a ingresar nota 4")


Promedio= (Nota_1 * 0.15 + Nota_2 * 0.35 + Nota_3 * 0.15 + Nota_4 * 0.35) 
print(f"Promedio final: {Promedio:.2f}")


if Promedio >= 4.0:
    print("Asignatura aprobada")
else:
    print("Asignatura reprobada")

if Promedio <1.0:
    print("Promedio fuera de rango")
if Promedio >7.0:
    print("Promedio fuera de rango")