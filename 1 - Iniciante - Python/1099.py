# 1099 - Soma de Ímpares Consecutivos II

valor = int(input())

for a in range(0, valor):
    entrada = input().split()
    A = int(entrada[0])
    B = int(entrada[1])
    contador = 0
    if A < B:
        for i in range((A + 1), B):
            if i % 2 != 0:
                contador = contador + i
    else:
        for i in range((B + 1), A):
            if i % 2 != 0:
                contador = contador + i 
    print(contador)