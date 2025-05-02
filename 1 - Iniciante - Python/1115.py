# 1115 - Quadrante

def quadrante():

    condicao = True

    while condicao:
        valor = input().split()
        x = int(valor[0])
        y = int(valor[1])
        if  x == 0 or y == 0:
            break
        if x > 0 and y > 0:
            print("primeiro")
        elif x < 0 and y > 0:
            print("segundo")
        elif x < 0 and y < 0:
            print("terceiro")
        elif x > 0 and y < 0:
            print("quarto")

quadrante()