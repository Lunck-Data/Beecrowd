# 1071 - Soma de Impares Consecutivos I

lista = []

for i in range(0, 2):
    lista.append(int(input()))

lista.sort()

A = lista[0]
B = lista[1]

total = 0

for i in range((1+A), B):
    if i % 2 == 1:
        total = total + i

print(total)