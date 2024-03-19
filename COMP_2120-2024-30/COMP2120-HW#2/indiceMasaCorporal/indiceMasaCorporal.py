# ingresar altura de la persona en metros
print("Ingrese la altura en metros:")
Altura = float(input())
# ingresar el peso de la persona en kilogramos
print("Ingrese el peso corporal en kilogramos:")
Peso = float(input())
# calcular el indice de masa de corporal usando la siguiente formula
IMC = Peso * 703 / (Altura * Altura)
# imprimir el resultado de indice de masa corporal
print("El indice de masa corporal es:", IMC)
