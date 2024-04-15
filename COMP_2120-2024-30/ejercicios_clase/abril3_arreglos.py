numeros = [5, 10, 15, 30, 40, 45, 50]
for i in range(7):
    print(numeros[i])

days = []
days.append("Domingo")
print(days)

meses = {}
meses[0] = "enero"
meses[1] = "febrero"
meses[2] = "marzo"
meses[3] = "abril"
meses[4] = "mayo"
meses[5] = "junio"
meses[6] = "julio"
meses[7] = "agosto"
meses[8] = "septiembre"
meses[9] = "octubre"
meses[10] = "noviembre"
meses[11] = "diciembre"
print(meses)
print("31 de " + meses[11])

unos = {}
for i in range(100):
    unos[i] = 1
salida = ""
for i in range(100):
    salida += str(unos[i]) + ", "
print(salida)
