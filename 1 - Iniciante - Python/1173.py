# 1173 - Preenchimento de Vetor I

vetor = []

vetor.append(int(input()))

for i in range (0,10):
    print(f"N[{i}] = {vetor[i]}")
    X = vetor[i] * 2
    vetor.append(X)