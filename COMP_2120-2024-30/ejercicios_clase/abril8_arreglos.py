# declarar de arreglos de tamaño 50; inicializados en el valor cero para todas sus posiciones.

# pseudocodigo:
# entero ceros [50];
# for i = 0 to 49, step = 1:
# 	ceros[i] = 0
# endfor

# declarar un arreglo en multiplos de 5 = {0, 5, 10, 15, 20, 25, 30,..., 100}

# pseudocodigo:
# entero multiplos5[200];
# for i = 0 to 200, step = 1
# 	multiplos5[i] = 5 * i
# endfor

cero = {}
for i in range(50):
    cero[i] = 0
# for i in range(50):
salida = ""
for i in range(50):
    salida = salida + str(cero[i]) + " "
print(salida)
print("-----------------------------------------------------")
multiplos5 = {}
for j in range(200):
    multiplos5[j] = 5 * j
salida2 = ""
for j in range(200):
    salida2 = salida2 + str(multiplos5[j]) + " "
print(salida2)
# ----------------------------------------------
# crear una funcion que imprima un arreglo de enteros

# pseucodigo:
# function imprimirArreglo(entero x[], entero size)
# 	str salida = ""
# 	entero i
# 	for i = 0 to size - 1, step = 1
# 		salida = salida + x[i]
# 	endfor
# 	display salida
# endfunction

# --------------------------------------------
# def imprimirArreglo(x, size):
#    salida3 = ""
#    for k in range(size - 1):
#        salida3 = salida3 + str(x[k]) + " "
#    print(salida3)


# print(imprimirArreglo(10, 200))
# ----------------------------------
def inicializar1(arreglox, size):
    for i in range(size):
        arreglox[i] = i + 1


# ---------------------------------
def inicializar2(arreglox, size):
    for i in range(size):
        arreglox[i] = 5 * i + 5


# ---------------------------------
