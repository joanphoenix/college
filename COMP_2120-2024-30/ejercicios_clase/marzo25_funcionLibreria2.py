# escriba un programa que simule el lanzamiento de un dado.

# Seria una funcion que no recibe parametros de entrada pero al invokarla, retorna un numero aleatorio entre 1 y 6.
#libreria
import random
# function Dado(): Entero
# 	declarar x es Entero
# 	x = randint(1, 6)
# 	return x
# endfunction

#codigo C++, java, C#
# entero Dado();

def Dado():
	x = random.randint(1, 6)
	return x
print(Dado())

# escriba un modulo que imprima el lanzamiento del dado 10 veces.

# Resumen:
# entrada: no tiene
# salida: no tiene
# proceso: repetir el print de dado 10 veces

# modulo repetirDado()
# 	for i = 1 to 10, step = 1
# 		print Dado()
# endmodulo

def repetirDado():
	for i in range(1, 11):
		print(Dado())
		
def repetirDadoH():
	cadena = ""
	for i in range(1, 11):
		cadena += str(Dado())
	print(cadena)
	
