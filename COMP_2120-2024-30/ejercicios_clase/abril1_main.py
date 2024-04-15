# import abril1_recursiva as lib1


# lib1.imprimir(10)
import math
from abril1_recursiva import fibonacci

# --------------------------------

# imprimir(10)
suma = 0
for i in range(1, 13):
    suma += 1 / fibonacci(i)
print(suma)
