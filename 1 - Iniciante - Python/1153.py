# 1153 - Fatorial Simples

valor = int(input())

fatorial = []

for i in range (0, valor):
    fatorial.append(valor-i)

soma = 1

for i in fatorial:
    soma = i * soma

print(soma)