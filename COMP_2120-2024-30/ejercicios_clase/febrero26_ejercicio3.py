# ingrese las notas
print("Ingrese las notas:")
notas = float(input())
# calcular la nota y fijarle un grado
if 90 <= notas and notas <= 100:
    print("La nota es A")
elif 80 <= notas and notas < 90:
    print("La nota es B")
elif 70 <= notas and notas < 80:
    print("La nota es C")
elif 60 <= notas and notas < 70:
    print("La notas es D")
else:
    print("La nota es F")
