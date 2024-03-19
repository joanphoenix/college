# escriba un programa que sume los multiplos de 7, comenzando en un valor inicial hasta un valor final. Donde el valor inicial y final lo ingresa el usuario.
# ejemplo: valor inicial = 25, valor final = 50
# 28 35 42 49
# mostrar en patalla: 154

# entrada: valor inicial y final
#


# pseudocodigo

# inicio
#
# fin

# ingresar el valor inicial
print("ingrese el valor inicial:")
valorInicial = int(input())
# ingresar el valor final
print("ingrese el valor final:")
valorFinal = int(input())
# ingrese el residuo deseado
print("ingrese el residuo:")
n = int(input())
# procesar la cadena
suma = 0
for i in range(valorInicial, valorFinal):
    if i % n == 0:
        suma += i
# imprimir la suma
print(suma)
