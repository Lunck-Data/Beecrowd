# 1172 - Substituição em Vetor I

vetor = []

for i in range(0, 10):
    X = int(input())
    if X <= 0:
        X = 1
    vetor.append(X)

for i in range(0, 10):
    print(f"X[{i}] = {vetor[i]}")
