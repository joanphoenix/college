# ---------------------librerias-----------------------------
def ventanaBordeLateral(vSize, hSize):
    for i in range(vSize):
        print("#" + " " * hSize + "#")


def ventanaBienvenida():
    print("#" * 60)
    ventanaBordeLateral(2, 58)
    print("#              Bienvenido al proyecto final                #")
    ventanaBordeLateral(2, 58)
    print("#              Nombre: Joan Rivera                         #")
    ventanaBordeLateral(2, 58)
    print("#              Numero de Estudiante: B00647718             #")
    ventanaBordeLateral(2, 58)
    print("#                     Version Final                        #")
    ventanaBordeLateral(2, 58)
    print("#  Para continuar inserte cualquier numero...              #")
    print("#" * 60)
    opcion = int(input("Input: "))
    return ventanaMenu(clientesActuales, maxCapacidad)


def ventanaMenu(clientesActuales, maxCapacidad):

    def espacioDisponible():
        return maxCapacidad - clientesActuales

    print("#" * 60)
    ventanaBordeLateral(2, 58)
    print("#                     Menu Principal                       #")
    ventanaBordeLateral(2, 58)
    print("#              [1] Entrada de cliente                      #")
    print("#              [2] Salida de cliente                       #")
    print("#              [3] Reiniciar conteo a cero                 #")
    print("#              [4] SALIR del programa                      #")
    ventanaBordeLateral(1, 58)
    if clientesActuales > 9:
        print(
            "#              Clientes en el local: ",
            clientesActuales,
            "                  #",
        )
    else:
        print(
            "#              Clientes en el local: ",
            clientesActuales,
            "                   #",
        )
    if espacioDisponible() < 10:
        print(
            "#              Espacios disponibles: ",
            espacioDisponible(),
            "                   #",
        )
    else:
        print(
            "#              Espacios disponibles: ",
            espacioDisponible(),
            "                  #",
        )
    ventanaBordeLateral(1, 58)
    print("# Ingrese el numero que se encuentra dentro de los [] para #")
    print("# ejecutar:                                                #")
    print("#" * 60)
    opcion = int(input("Input: "))
    while opcion >= 0:
        if opcion == 1:
            clientesActuales = clientesActuales + 1
            ventanaMenu(clientesActuales, maxCapacidad)
        elif opcion == 2:
            clientesActuales = clientesActuales - 1
            ventanaMenu(clientesActuales, maxCapacidad)
        elif opcion == 3:
            clientesActuales = 0
            ventanaMenu(clientesActuales, maxCapacidad)
        elif opcion == 4:
            ventanaSalida()


def ventanaSalida():
    print("#" * 60)
    ventanaBordeLateral(2, 58)
    print("#              Ventana de confirmar salida                 #")
    ventanaBordeLateral(2, 58)
    print("#              [0] Cancelar y volver al menu               #")
    ventanaBordeLateral(1, 58)
    print("#              [4] Confirmar salida                        #")
    ventanaBordeLateral(5, 58)
    print("# Ingrese el numero que se encuentra dentro de los []      #")
    print("# para ejecutar:                                           #")
    print("#" * 60)
    opcion = int(input("Input: "))
    if opcion == 4:
        print("#" * 36)
        ventanaBordeLateral(2, 34)
        print("#  ¡Gracias por usar el programa!  #")
        ventanaBordeLateral(2, 34)
        print("#" * 36)
        exit()
    elif opcion == 0:
        return ventanaMenu(clientesActuales, maxCapacidad)


# -------------------main-----------------------------
clientesActuales = 0
maxCapacidad = 60
opcion = 0

ventanaBienvenida()
