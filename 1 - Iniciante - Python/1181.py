# 1181 - Linha na Matriz

m=[]
valorMatriz = int(input())

operacao = input()

for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)
    
soma = 0

for i in range(12):
    soma = soma + m[valorMatriz][i]

if operacao == "S":
    print(f"{soma:.1f}")
else:
    print(f"{soma/12:.1f}")