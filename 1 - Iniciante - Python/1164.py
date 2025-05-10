# 1164 - Número Perfeito

N = int(input())

for i in range(0, N):
    X = int(input())

    perfeito = 0
    for a in range(1,X):
        if X / a == X //a:
            perfeito += a

    if perfeito == X:
        print(f"{X} eh perfeito")
    else:
        print(f"{X} nao eh perfeito")
