# 1072 - Intervalo 2

A = int(input())

lista = []

for i in range(0, A):
    lista.append(int(input()))

ini = 0
out = 0

for i in lista:
    if i >= 10  and i <= 20:
        ini += 1
    else:
        out += 1

print(f"{ini} in")
print(f"{out} out")