# 1174 - Seleção em Vetor I

vetor = []

for i in range(0,100):
    vetor.append(float(input()))

for i in range(0, 100):
    if vetor[i] <= 10:
        print(f"A[{i}] = {vetor[i]}")