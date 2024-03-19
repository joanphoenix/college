# Solicitar el largo y ancho del primer rectángulo
print("Introduce el largo del primer rectángulo:")
largo1 = float(input())
print("Introduce el ancho del primer rectángulo:")
ancho1 = float(input())
# Solicitar el largo y ancho del segundo rectángulo
print("Introduce el largo del segundo rectángulo:")
largo2 = float(input())
print("Introduce el ancho del segundo rectángulo:")
ancho2 = float(input())
# Calcular el área de ambos rectángulos
area1 = largo1 * ancho1
area2 = largo2 * ancho2
# Comparar los rectángulos y mostrar el resultado
if area1 > area2:
    print("El primer rectángulo tiene un área mayor.")
else:
    if area1 < area2:
        print("El segundo rectángulo tiene un área mayor.")
    else:
        print("Ambos rectángulos tienen la misma área.")
