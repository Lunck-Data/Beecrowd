# 1150 - Ultrapassando Z


def ultrapassando():

    X = int(input())

    Y = 0

    while X >= Y:
        Y = int(input())

    soma = 0
    quantia = 0

    for i in range(0, 1000):
        soma += X + i
        quantia += 1
        if soma > Y:
            return print(quantia)
        
ultrapassando()