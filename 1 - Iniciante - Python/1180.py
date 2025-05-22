# 1180 - Menor e Posição

vetor = int(input())

valoresVetor = input().split()

listona = []

for i in valoresVetor:
    listona.append(int(i))

menor = listona[0]
posicao = 0

for i in range(0, vetor):
    if listona[i] < menor:
        menor = listona[i]
        posicao = i

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")