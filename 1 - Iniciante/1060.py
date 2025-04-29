# 1060 - Números Positivos

lista = []

for i in range(0, 6):
    lista.append(float(input()))

contador = 0

for i in lista:
    if i > 0:
        contador += 1

print(f"{contador} valores positivos")