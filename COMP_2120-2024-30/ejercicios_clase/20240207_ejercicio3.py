# Realizar un programa que transforme la temperatura de grados
# fahrenheit a grados centigrados.

# Donde la entrada es la variable F-fahrenheit.

# C = 5/9*(F-32)

# -Resumen:

# input:
# F = Real

# output:
# C = Real

# proceso:
# Calcular usando la formula.
# C = 5/9*(F-32)


# -Pseudocodigo

# inicio: declarar variables
# declarar que F, C son tipo Real
# solicitar la entrada del valor a las variables: F, C
# enviar mensaje de declaracion de las variables:
# print "ingrese la temperatura en grados F:"
# entrada del valor de F
# Realizar un proceso matematico para transformar el valor de F a
# centigrados:
# C =  5/9*(F-32)
# Salida:
# Mostrar el resultado del proceso matematico de F guardado en C
# print 'la temperatura de Fahrenheit a centigrados seria:',C

# -Codigo en python

# Declarar tipo de variables


# Declarar el valor de F

print(
    "Para convertir la temperatura a Celsius, ingrese la temperatura en grados Fahrenheit:"
)
F = float(input())

# Tranformar la temperatura Fahrenheit a Celsius con proceso matematico
# guardado en la variable C

print("Transformando de Fahrenheit a Celsius...")

C = float(5.0 / 9.0 * (F - 32.0))

# Mostrar el resultado de la transformacion de F a C

print("La temperatura en centigrados es:", C)
