# function f(real x, entero n): Real
# 	if n == 1 then
# 		return 1
# 	else
# 		returnx x * f(x, n - 1)
# 	endif
# end function

# modulo imprimir(entero n)
# 	if n ==1 then
# 		display "-"
# 	else 
# 		display "-"
# 		imprimir(n - 1)
# 	endif
# endmodulo\
def imprimir(n):
	if n == 1:
		print("-")
	else:
		print("-")
		

		

# fibonacci
#f(n) = f(n - 1) + f(n - 2)
# 	f(1) = 1
# 	f(2) = 1

def fibonacci(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)
#---------------main-------------------	
x = fibonacci(6)
print(x)
