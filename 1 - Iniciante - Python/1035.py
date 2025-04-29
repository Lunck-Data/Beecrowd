# 1035 - Teste de Seleção 1

valor = input().split()

A = int(valor[0])
B = int(valor[1])
C = int(valor[2])
D = int(valor[3])

moduloA = A % 2

somaCD = C + D
somaAB = A + B

if B > C and D > A and somaCD > somaAB and C > 0 and D > 0 and moduloA == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")