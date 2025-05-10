# 1177 - Preenchimento de Vetor II

T = int(input())

vetor = []

vezes = 1000 // T
sobra = 1000 % T

totalVezes = vezes + sobra

for i in range(0, totalVezes):
    for i in range(0, T):
        vetor.append(i)

for i in range(0, 1000):
    print(f"N[{i}] = {vetor[i]}")