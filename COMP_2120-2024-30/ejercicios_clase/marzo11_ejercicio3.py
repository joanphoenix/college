# solicitar el valor entero
print("ingrese el numero entero:")
# leer el valor entero
n = int(input())
# procesar la cadena
for j in range(1, n + 1):
    # definir cadena dentro del primer for
    cadena1 = ""
    for i in range(1, j + 1):
        cadena1 = cadena1 + "*"
    print(cadena1)
