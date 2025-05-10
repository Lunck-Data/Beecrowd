# 1175 - Troca em Vetor I

vetor = list(range(0,20))

for i in range(1, 21):
    X = int(input())
    indice = 20-i
    vetor[indice] = X

for i in range(0,20):
    print(f"N[{i}] = {vetor[i]}")