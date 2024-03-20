# Hacer una rutina o funcion que imprima un triangulo con sus lados de tamaño n, con el prototipo de modulo impTriangulo(integer n)
# ejemplo: si invoca el modulo
# impTriangulo(3)
# *
# **
# ***
# Resumen:
# entrada: n es entero
# salida: no tiene
# proceso: escribalo en sus palabras

# pseudocodigo

# 1
# inicio
# module impTriangulo(integer n)
# 	declarar j, i son integer
# 	declarar cadena1 es string
# 	for j = 1 to n, step = 1
# 		cadena1 = ""
# 		for i = 1 to j, step = 1
# 			cadena1 += "*"
# 		endfor
# 		display cadena1
# 	endfor
# endmodule
# fin

# 2
# escriba una funcion que devuelva de el resultado de la siguiente formula:
# factorial(n) = 1 * 2 * 3 * 4 * 5 *...* n

# resumen

# entrada: n es entero
# salida: resultado es entero
# proceso: utilizando un ciclo, se acumulara las multiplicaciones de 1 hasta n en resultado.

# psedocodigo

# inicio
# function factorial(integer n): integer
# 	declarar resultado, contador es entero
# 	contador = 1
# 	resultado = 1
# 	while(contador <= n)
# 		resultado = resultado * contador
# 		contador += 1
# 	endwhile
# 	return resultado
# endfunction
# fin


# variables globales


# funciones
def impTriangulo(n):
    i = 0
    j = 0
    cadena1 = ""
    for j in range(1, n + 1):
        cadena1 = ""
        for i in range(1, j + 1):
            cadena1 += "*"
        print(cadena1)


# main
impTriangulo(10)


#
def factorial(n):
    contador = 1
    resultado = 1
    while contador <= n:
        resultado = resultado * contador
        contador = contador + 1
    return resultado


print(factorial(4))
