# variables globales


# funciones y rutinas
def ventana1():
    print("##############################")
    print("#                            #")
    print("#                            #")
    print("#                            #")
    print("#                            #")
    print("#                            #")
    print("#                            #")
    print("#                            #")
    print("#                            #")
    print("#                            #")
    print("#                            #")
    print("#                            #")
    print("##############################")


def ventana1v2():
    print("##############################")
    for i in range(11):
        print("#                            #")
    print("##############################")


def ventana1v3(x):
    strcadena = ""
    for i in range(x):
        strcadena += "#"
    print(strcadena)
    strcadena2 = "#"
    for i in range(x - 2):
        strcadena2 += " "
    strcadena2 += "#"
    for i in range(11):
        print(strcadena2)
    print(strcadena)


def ventana2v1():
    print("##############################")
    print("#                            #")
    print("#                            #")
    print("#                            #")
    print("#                            #")
    print("#        Bienvenidos         #")
    print("#             a              #")
    print("#          comp2120          #")
    print("#                            #")
    print("#                            #")
    print("#                            #")
    print("#                            #")
    print("##############################")


# funcion suma
# pseudocodigo
# function sumar
#   declarar y, i son Enteros
#   y = 0
#   for i = 1 to 5000, step = 1
#       y += i
#   endfor
#   return y
# endfunction
def sumar():
    y = 0
    for i in range(1, 5001):
        y += i
    return y


def sumarv2(x, y):
    z = 0
    for i in range(x, y):
        z += i
    return z


# main program
w = sumarv2(20, 600)
print(w)
