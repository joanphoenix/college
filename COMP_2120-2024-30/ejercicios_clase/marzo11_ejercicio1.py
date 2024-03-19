# escriba un programa que imprima n-veces el simbolo de asterisco (*)
# donde n es el valor de entrada.
# ejemplo si n = 4
#  ****
# si n = 12
# ************
# inicio
# declarar n,i es entero
# declarar cadena1 es texto
# imprimir "ingrese un valor entero"
# cadena1 = ""
# leer n
# para i = 1 hasta n, pasos = 1
# 	cadena1 = cadena1 + "*"
# finpara
# imprimir cadena1
# fin

# solicitar el valor
print("ingrese un valor entero:")
# definir cadena
cadena1 = ""
# leer el valor entero
n = int(input())
# procesar cadena
for i in range(1, n + 1):
    cadena1 = cadena1 + "*"
# mostrar resultado de cadena
print(cadena1)


# escriba un programa que imprima los numeros del 1 hasta n, donde n
# es el valor de entrada:
# ejemplo si n = 4
# 1, 2, 3, 4
# si n = 11
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

# solicitar el valor entero
print("ingrese un valor entero:")
# declarar cadena
cadena2 = ""
# leer el valor entero
n1 = int(input())
# procesar cadena
for j in range(1, n1 + 1):
    cadena2 = cadena2 + str(j) + ", "
print(cadena2)
