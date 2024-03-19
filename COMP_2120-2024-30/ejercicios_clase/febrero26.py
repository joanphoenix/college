# Programa para sueldo por hora de part timer

# inicio

# declarar variables

# totalPago,tiempo son reales

# solicitar tiempo trabajado

print("Ingrese las horas trabajadas:")
tiempo = float(input())

# calcular el sueldo por hora (9.50) y su exceso por encima de 20hrs(11.25)

if tiempo <= 20:
    totalPago = tiempo * 9.50
    print("Total a pagar seria:", totalPago)
else:
    if tiempo > 20:
        totalPago = 20 * 9.50 + (tiempo - 20) * 11.25
        print("Total a pagar seria:", totalPago)

# mostrar el resultado de total a pagar
# terminar programa
