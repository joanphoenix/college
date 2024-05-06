# Realizar un programa que reciba de entrada un valor numerico real y
# y que realice e imprima el resultado de las siguientes operaciones:

# x + 3
# x * x + 2
# 1 - x / x + 1
# 1 + 1 / 1 + 1 / x

# Resume:

# Input: x es real

# output: y, z, u, son reales

# proceso: calcular

# y= x + 3
# z= x * x + 2
# u= (1 - x) / (x + 1)
# w= 1 + 1 / (1 + 1 / x)

# imprimir resultados

# Declarar variables: x, y, z, u, w son reales
print("ingrese un valor numerico real")
x = float(input())


y = x + 3

z = x * x + 2

u = (1 - x) / (x + 1)

w = 1 + 1 / (1 + 1 / x)

# print 'El resultado de la primera operacion es:', y
# print 'El resultado de la segunda operacion es:', z

print("El resultado de la primera operacion es:", y)
print("El resultado de la segunda operacion es:", z)
print("El resultado de la tercera operacion es:", u)
print("El resultado de la cuarta operacion es:", w)
