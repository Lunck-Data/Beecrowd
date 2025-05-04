# 1154 - Idades

lista = []

while True:

    A = int(input())
    if A < 0:
        break
    lista.append(A)

soma = 0
divisor = 0

for i in lista:
    soma = soma + i
    divisor += 1

resultado = soma / divisor

print(f"{resultado:.2f}")