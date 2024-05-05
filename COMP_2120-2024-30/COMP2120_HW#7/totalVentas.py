"""start
        
        declare int ventas[7] = 0, 0, 0, 0, 0, 0, 0
        declare int total = 0
        for i = 0 to 6, step = 1
            display("Entre ventas para el dia ", i + 1, ": ")
            ventas[i] = int(input())
            total = total + ventas[i]
        endfor

        display("Total de ventas en la semana: ", total)

    end"""

ventas = [0, 0, 0, 0, 0, 0, 0]
total = 0
for i in range(7):
    print("Entre ventas para el dia ", i + 1, ": ")
    ventas[i] = int(input())
    total += ventas[i]

print("Total de ventas en la semana: ", total)
