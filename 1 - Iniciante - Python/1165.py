# 1165 - Número Primo

N = int(input())

for i in range(0, N):
    X = int(input())
    contador = 0
    for a in range(1,(X + 1)):
        if X / a == X // a:
            contador += 1
    if contador == 2:
        print(f"{X} eh primo")
    else:
        print(f"{X} nao eh primo")