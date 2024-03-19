# ingresar las grasas consumidas
print("Ingrese las grasas consumidas:")
Grasas = float(input())
# ingresar los carbohidratos consumidos
print("Ingrese los carbohidratos consumidos:")
Carbohidratos = float(input())
# calcular las calorias usando las grasas consumidas
Calorias_Grasa = float(Grasas * 9)
# calcular las calorias usando los carbohidratos consumidos
Calorias_Carbohidratos = float(Carbohidratos * 4)
# imprimir el total de calorias consumidas por grasa y carbohidratos consumidos
print(
    "El total de calorias consumidas es:",
    Calorias_Grasa,
    "calorias por grasas y",
    Calorias_Carbohidratos,
    "calorias por carbohidratos; por lo tanto, el total de calorias consumidas es:",
    Calorias_Grasa + Calorias_Carbohidratos,
    "calorias.",
)
