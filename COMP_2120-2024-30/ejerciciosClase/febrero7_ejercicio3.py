# Realizar un programa que transforme la temperatura de grados
# Fahrenheit a grados centígrados.

# Donde la entrada es la variable F-Fahrenheit.

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
# enviar mensaje de declaración de las variables:
# print "ingrese la temperatura en grados F:"
# entrada del valor de F
# Realizar un proceso matemático para transformar el valor de F a
# centígrados:
# C =  5/9*(F-32)
# Salida:
# Mostrar el resultado del proceso matemático de F guardado en C
# print 'la temperatura de Fahrenheit a centígrados seria:',C

# -Código en python

# Declarar tipo de variables


# Declarar el valor de F

print(
    "Para convertir la temperatura a Celsius, ingrese la temperatura en grados Fahrenheit:"
)
F = float(input())

# Transformar la temperatura Fahrenheit a Celsius con proceso matemático
# guardado en la variable C

print("Transformando de Fahrenheit a Celsius...")

C = float(5.0 / 9.0 * (F - 32.0))

# Mostrar el resultado de la transformación de F a C

print("La temperatura en centígrados es:", C)
