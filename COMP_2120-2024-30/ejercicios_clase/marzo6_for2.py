# suma
# inicio
# suma = 0
# for contador = 1 to 10, step = 1
# 	suma = suma + contador
# endfor
# print "la suma es", suma
# end
print("---------for-------------")
suma = 0
for contador in range(1, 11):
    suma = suma + contador
print("la suma es", suma)
print("---------while------------")
suma = 0
contador = 1
while contador < 11:
    suma = suma + contador
    contador = contador + 1
print("la suma es", suma)
