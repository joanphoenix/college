def rutina1():
    cadena1 = ""
    for i in range(1, 11):
        cadena1 = cadena1 + "*"
    print(cadena1)


def fun1(name, lname, age):
    print(name + " " + lname + " tiene " + str(age) + " años.")


lname = "Hernandez"
age = 23
rutina1()
fun1("Javier", lname, age)
