# 1157 - Divisores I

valor = int(input())

lista = []

for i in range (1, (valor+1)):
    dividido = valor // i
    if dividido == valor / i:
        print(i)