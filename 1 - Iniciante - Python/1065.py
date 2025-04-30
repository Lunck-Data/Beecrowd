# 1065 - Pares entre Cinco Números

lista = []

for A in range(0, 5):
    A = int(input())
    lista.append(A)

contador = 0

for B in lista:
    teste = B % 2
    if teste == 0:
        contador += 1

print(f"{contador} valores pares")