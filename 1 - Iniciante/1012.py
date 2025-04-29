# 1012 - Área

dados = input().split()

A = float(dados[0])
B = float(dados[1])
C = float(dados[2])

pi = 3.14159

TRIANGULO = (A * C) / 2 # A = base * altura /2
CIRCULO = pi * C ** 2 # A = π * raio²
TRAPEZIO = (A + B) * C / 2 # A=(base maior + base menor ) altura /2
QUADRADO = B ** 2 # a = lado ** 2
RETANGULO = A * B # A = base x altura

print(f"TRIANGULO: {TRIANGULO:.3f}")
print(f"CIRCULO: {CIRCULO:.3f}")
print(f"TRAPEZIO: {TRAPEZIO:.3f}")
print(f"QUADRADO: {QUADRADO:.3f}")
print(f"RETANGULO: {RETANGULO:.3f}")