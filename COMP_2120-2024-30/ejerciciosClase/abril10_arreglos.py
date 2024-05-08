# A ={1 to 100}
import random


# ------------------------------------

# crear una funcion que inicialize el arreglo de la siguiente forma:
# pseudocodigo
# entero A[100]
# crear funcion:
# module inicializar1(entero A[], entero size)
# 	entero i
# 	for i = 0 to size - 1, step = 1
# 		A[i] = 5 * i + 5
# 	endfor
# endmodule


# ----------------------------------------------------
def inicializar1(A, size):
    A = {}
    for i in range(size):
        A[i] = 5 * i + 5
    salida = ""
    for i in range(size):
        salida = salida + str(A[i]) + " "
    print(salida)


# ----------------------------------------------------
# module inicializarRand(entero x[],entero size)
# 	entero i
# 	for i = 0 to size, step = 1
# 		x[i] = randint(1, 6)
# 	endfor
# endmodule
# ----------------------------------------------------
def inicializarRand(x, size):
    for i in range(size):
        x[i] = random.randint(1, 6)


# ----------------------------------------------------
# Crear una funcion que sume todos los valores de un arreglo y que devuelva la suma:
# prototipo:
# function sumaArreglo(entero A[], entero size): entero
# ejemplo: A = {1, 4, 6, 8, 2, 4, 6}
# la suma = 31
# ---------
# 	sum = sum + A[0]
# 	sum = sum + A[1]
# 	sum = sum + A[2]
# ---------
# 	entero i, sum = 0
# 	for i = 0 to size, step = 1
# 		sum = sum + A[i]
# 	endfor
# 	return sum
# endfunction
# ------------------------------------------------------
# def sumaArreglo(A, size):

# -----------------------------------------------------
# Crear una funcion que calcule el promedio de todos los elementos de un arreglo de reales, de tamaño N.
# prototipo:
# function promedioArreglo(real x[], entero size): real
# escriba la funcion:
