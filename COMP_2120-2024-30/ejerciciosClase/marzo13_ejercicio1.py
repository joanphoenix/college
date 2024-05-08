# escriba un programa que imprima una linea de 40 chars donde los ultimos n elementos sean *, y los primeros sean ""
# ejemplo: si n = 10
# _________*
# resumen
# entrada: n entero
# salida:no tiene
# proceso:usando un ciclo se acumula 40-n veces el simbolo # usando un ciclo for se acumula 10 veces el simbolo *

# pseudocodigo
# inicio
# declarar n,i es Entero
# declarar cadena1 es texto
# imprimir "ingrese la variable de entrada"
# leer n
# cadena1 = ""
# para i = 1 hasta 40 - n, saltos de 1 entonces
# 	cadena1 = cadena1 + " "
# finpara
# para i = 1 hasta n, saltos de 1 entonces
# 	cadena1 += "*"
# finpara
# imprimir cadena1
# fin

# ingresar le valor numerico
print("ingrese el numero:")
# leer el numero
n = int(input())
# declarar cadena
cadena1 = ""
# procesar la cadena
for i in range(1, 40 - n + 1):
    cadena1 = cadena1 + "#"
for i in range(1, n + 1):
    cadena1 = cadena1 + "*"
print(cadena1)
