# 1159 - Soma de Pares Consecutivos

condicao = True

while condicao:
    X = int(input())

    if X == 0:
        condicao = False
        break

    soma = 0

    if not X % 2 == 0:
        X += 1

    for i in range(0, 5):
        soma = soma +(X + (2 * i))
        
    print(soma)