# 1017 - Gasto de Combustível

horas = int(input())
velocidade = int(input())

kmL = 12

distancia = velocidade * horas

Litros_necessario = distancia / kmL

print(f"{Litros_necessario:.3f}")