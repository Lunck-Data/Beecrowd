# 1133 - Resto da Divisão

lista = []

lista.append(int(input()))
lista.append(int(input()))

lista.sort()

A = lista[0]
B = lista[1]

for i in range((A+1), B):
    if i % 5 == 2 or i % 5 == 3:
        print(i)