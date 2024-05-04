# matrices

# entero A[4][6]

# Real C[3][18]
# for i = 0 to 1, step = 1
# 	for j = 0 to 17, step = 1
# 		B[i][j] = 0
# 	endfor
# endfor
# for j = 0 to 1, step = 1
# 	C[2][j] = 1
# endfor

# imprimir una matriz A[][] de 4 x 5

# for i = 0 to 3 , step = 1
# 	salida = ""
# 	for j = 0 to 4, step = 1
# 		salida = salida + str(A[i][j]) + " "
# 	endfor
# 	display salida
# endfor

# matriz de 3 x 3-----------------------------
A = [[1, 2, 3], [0, 0, 0], [3, 5, 7]]
for i in range(3):
    salida = ""
    for j in range(3):
        salida = salida + str(A[i][j]) + " "
    print(salida)
# ---------------------------------------------
# F = 4 x 18
