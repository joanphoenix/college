"""function insArregloOrdenado(int A[], int Size):
	int i, temp, j 
	for i = 0 to Size - 1, step = 1
		display "ingrese el valor"
		input temp
		j = i
		for j = 0 to i - 1, step = 1
			if temp < A[k] then
				j = k
				break
			endif
		for k = i -1 to j, step = 1
			A[k + 1] = A[k] 
		endfor
		A[j] = temp
		endfor
	endfor
endfunction"""

A = {5, 8, 2, 1, 7, 4, 6, 3}


def insArregloOrdenado(A, Size):
    temp = 0
    for i in range(Size - 1):
        print("ingrese el valor:")
        temp = input()
        j = i
        for j in range(i - 1):
            if temp < A[k]:
                j = k
                break
        for k in range(i - 1, j):
            A[k + 1] = A[k]
        A[j] = temp
        return A


print(insArregloOrdenado(A, 8))
