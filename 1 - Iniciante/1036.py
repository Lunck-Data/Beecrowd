# 1036 - Fórmula de Bhaskara

import math

valores = input().split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

def bhaskara(A, B, C):

    delta = B ** 2 - 4 * A * C

    if A == 0 or delta < 0:
        return print("Impossivel calcular")

    R1 = (-B + math.sqrt(delta)) / (2 * A)
    R2 = (-B - math.sqrt(delta)) / (2 * A)

    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")

bhaskara(A, B, C)