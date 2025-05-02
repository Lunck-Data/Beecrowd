# 1132 - Múltiplos de 13

lista = []

lista.append(int(input()))
lista.append(int(input()))

lista.sort()

A = lista[0]
B = lista[1]

total = 0

for i in range(A, (B+1)):
    div = i / 13
    divInt = i // 13

    if not div == divInt:
        total += i

print(total)