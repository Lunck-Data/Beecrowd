# 1043 - Triângulo

valores = input().split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

AB = A + B
BC = B + C
CA = C + A

if AB > C and BC > A and CA > B:
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = (A + B) * C / 2 #A=(a+b)h/2
    print(f"Area = {area:.1f}")