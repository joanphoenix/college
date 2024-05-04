def funCubos(x):
    cont = 1
    for i in range(3):
        cont = cont + 3 * x * i
    return cont


print(funCubos(4))
