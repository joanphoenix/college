# solicitar la masa del objeto
print("Introduce la masa del objeto en kilogramos:")
masa = float(input())
# calcular el peso del objeto usando la formula
peso = masa * 9.81
# comparar el peso y mostrar el resultado
if peso > 1000:
    print("El objeto es muy pesado.")
else:
    if peso < 10:
        print("El objeto es muy liviano.")
    else:
        print("El peso del objeto es normal.")
