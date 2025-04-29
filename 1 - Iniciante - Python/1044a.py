# 1044 - Múltiplos

valores = input().split()

A = int(valores[0])
B = int(valores[1])

tester1 = B / A
tester2 = B // A

tester3 = A / B
tester4 = A // B

if tester1 == tester2 or tester3 == tester4:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")