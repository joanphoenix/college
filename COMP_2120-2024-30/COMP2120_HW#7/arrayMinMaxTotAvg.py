"""start

        declare int valores[20] = 0
        declare int min = 0
        declare int max = 0
        declare int total = 0
        declare int promedio = 0
        for i = 0 to 19, step = 1
            display("Entre el valor ", i + 1, ": ")
            valores[i] = int(input())
            if i = 0
                min = valores[i]
                max = valores[i] 
            endif
            if valores[i] < min
                min = valores[i]
            endif
            if valores[i] > max
                max = valores[i]
            endif
            total = total + valores[i]
        endfor
        promedio = total / 20
        display("Min valor: ", min)
        display("Max valor: ", max)
        display("Total: ", total)
        display("Promedio: ", promedio)
    end"""

valores = [0] * 20
min = 0
max = 0
total = 0
promedio = 0

for i in range(20):
    print("Enter el valor ", i + 1, ": ")
    valores[i] = int(input())
    if i == 0:
        min = valores[i]
        max = valores[i]
    if valores[i] < min:
        min = valores[i]
    if valores[i] > max:
        max = valores[i]
    total += valores[i]

promedio = total / 20

print("Min valor: ", min)
print("Max valor: ", max)
print("Total: ", total)
print("Average: ", promedio)
