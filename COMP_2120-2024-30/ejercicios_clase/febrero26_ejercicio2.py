# Programa para sueldo por hora de part timer

# inicio
print("Ingrese las horas trabajadas:")
tiempo = float(input())
# calcular el sueldo por hora (9.50) y su exceso por encima de 20hrs(11.25)
if tiempo <= 20:
    totalPago = tiempo * 9.50
elif tiempo > 20:
    totalPago = 20 * 9.50 + (tiempo - 20) * 11.25
# mostrar el resultado de total a pagar
print("Total a pagar a seria:", float(totalPago))
# terminar programa
