# libreria
import math
# escriba una funcion que calcule la hipotenusa de un triangulo rectangulo, donde los catetos son la entrada.
# hip = raizCuadrada(a * a + b * b)
# resumen
# entrada: a,b es Real
# salida: Real hipot
# proceso:retornar el valor calculado hipot = sqrt(a * a + b * b)

# function hipotenusa(real a, real b): real
# 	declarar hipotenusa es Real
# 	hipot = sqrt(a * a + b * b)
# 	return hipot	
# endfunction

def hipotenusa(a,b):
	hipot = math.sqrt(a * a + b * b)
	return hipot
print(hipotenusa(3,4))

