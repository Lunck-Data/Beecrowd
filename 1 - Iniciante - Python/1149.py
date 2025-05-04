# 1149 - Somando Inteiros Consecutivos

valores = input().split()

lista = []

for i in valores:
    A = int(i)
    lista.append(A)

A = lista[0]
lista.remove(lista[0])
N = 0

for i in lista:
    if i >= 0:
        N = i

soma = 0

for i in range(0, N):
    soma = soma + (A + i)

print(soma)