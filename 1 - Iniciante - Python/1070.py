# 1070 - Seis Números Ímpares

valor = int(input())

for i in range(valor, (valor+12)):
    if i % 2 == 1:
        print(i)