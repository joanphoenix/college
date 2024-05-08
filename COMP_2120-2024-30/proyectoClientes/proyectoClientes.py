# ---------------------librerias-----------------------------
def windowSideBorder(vSize, hSize):
    for i in range(vSize):
        print("#" + " " * hSize + "#")


def ventanaBienvenida():
    print("#" * 60)
    windowSideBorder(2, 58)
    print("#              Bienvenido al proyecto final                #")
    windowSideBorder(2, 58)
    print("#              Nombre: Joan Rivera                         #")
    windowSideBorder(2, 58)
    print("#              Numero de Estudiante: B00647718             #")
    windowSideBorder(2, 58)
    print("#                     Version Final                        #")
    windowSideBorder(2, 58)
    print("#  Para continuar inserte cualquier numero...              #")
    print("#" * 60)


def ventanaMenu():
    print("#" * 60)
    windowSideBorder(2, 58)
    print("#                     Menu Principal                       #")
    windowSideBorder(2, 58)
    print("#              [1] Entrada de cliente                      #")
    print("#              [2] Salida de cliente                       #")
    print("#              [3] Reiniciar conteo a cero                 #")
    print("#              [4] SALIR del programa                      #")
    windowSideBorder(1, 58)
    print(
        "#              Clientes en el local", clientesActuales, "                    #"
    )
    print("#              Espacios disponibles", maxCapacidad, "                    #")
    windowSideBorder(1, 58)
    print("# Ingrese el numero que se encuentra dentro de los [] para #")
    print("# ejecutar:                                                #")
    print("#" * 60)


def ventanaSalida():
    print("#" * 60)
    windowSideBorder(2, 58)
    print("#              Ventana de confirmar salida                 #")
    windowSideBorder(2, 58)
    print("#              [0] Cancelar y volver al menu               #")
    windowSideBorder(1, 58)
    print("#              [4] Confirmar salida                        #")
    windowSideBorder(5, 58)
    print("# Ingrese el numero que se encuentra dentro de los []      #")
    print("# para ejecutar:                                           #")
    print("#" * 60)


# -------------------main-----------------------------
clientesActuales = 0
maxCapacidad = 60
opcion = 0
ventanaBienvenida()
opcion = input(int())
while opcion > 0:
    ventanaMenu()
    input(opcion)
    if opcion == 1:
        clientesActuales = clientesActuales + 1
    elif opcion == 2:
        clientesActuales = clientesActuales - 1
    elif opcion == 3:
        clientesActuales = 0
    elif opcion == 4:
        ventanaSalida()
        input(opcion)
