# 1045 - Tipos de Triângulos

valores = input().split()

valores_novo = []

for i in valores:
    valores_novo.append(float(i))

valores_novo.sort(reverse=True)

A = valores_novo[0]
B = valores_novo[1]
C = valores_novo[2]

if A >= B+C:
    print("NAO FORMA TRIANGULO")
elif (A ** 2) == (B ** 2 + C ** 2):
    print("TRIANGULO RETANGULO")
elif (A ** 2) > (B ** 2 + C ** 2):
    print("TRIANGULO OBTUSANGULO")
elif (A ** 2) < (B ** 2 + C ** 2):
    print("TRIANGULO ACUTANGULO")

if A == B == C:
    print("TRIANGULO EQUILATERO")
elif A == B or B == C or C == A:
    print("TRIANGULO ISOSCELES")