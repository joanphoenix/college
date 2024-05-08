# ingresar el valor
print("ingrese el numero:")
n = int(input())
# procesar cadena
for j in range(1, n + 1):
    # declarar cadena
    cadena1 = ""
    for i in range(1, n - j + 1):
        cadena1 = cadena1 + " "
    for i in range(1, j + 1):
        cadena1 = cadena1 + "*"
    # imprimir cadena1
    print(cadena1)
