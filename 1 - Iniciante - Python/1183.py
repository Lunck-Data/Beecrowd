# 1183 - Acima da Diagonal Principal

m = []

operacao = input().upper()

for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

soma = 0
coluna = 1
contador = 0

for i in range(12):
    for j in range(coluna,12):
        soma += m[i][j]
        contador += 1
    coluna += 1

if operacao == "S":
    print(f"{soma:.1f}")
elif operacao == "M":
    print(f"{soma/contador:.1f}")