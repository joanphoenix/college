# escriba un programa que ingrese un valor entero n e imprima las
# siguientes formas:
# n = 4
# for i = 1 to 4

# solicitar el valor entero
print("ingrese el numero entero:")
# leer el valor entero
n = int(input())
# procesar la cadena
for j in range(1, n + 1):
    # definir cadena dentro del primer for
    cadena1 = ""
    for i in range(1, n + 1):
        cadena1 = cadena1 + "*"
    print(cadena1)
