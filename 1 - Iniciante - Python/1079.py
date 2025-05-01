# 1079 - Médias Ponderadas

valor = int(input())

for i in range(0, valor):
    lista = input().split()
    A = float(lista[0])
    B = float(lista[1])
    C = float(lista[2])

    media = ((A * 0.2) + (B * 0.3) + (C * 0.5))

    print(f"{media:.1f}")