# solicitar al usuario la cantidad de paquetes comprados
print("Introduce la cantidad de paquetes de software comprados:")
cantidad = int(input())
# definir el precio del paquete de software
precio = 100
# determinar el descuento basado en la cantidad de paquetes comprados
if cantidad >= 100:
    descuento = 0.50
else:
    if cantidad >= 50:
        descuento = 0.40
    else:
        if cantidad >= 20:
            descuento = 0.30
        else:
            if cantidad >= 10:
                descuento = 0.20
            else:
                descuento = 0
# calcular el total de la compra
total = precio * cantidad * (1 - descuento)
# mostrar el descuento y el total de la compra
if descuento > 0:
    print(
        "Tiene un descuento del",
        descuento * 100,
        "% de su compra que tenia un total de $",
        precio * cantidad,
    )
print("El total final de su compra es: $", total)
