print("Ingrese el valor de x:")
x = float(input())
if x < -5:
    y = x + 1
else:
    if -5 <= x < 10:
        y = x * x
    else:
        if x >= 10:
            y = -3
print("Salida de y =", y)