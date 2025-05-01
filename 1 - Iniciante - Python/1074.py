# 1074 - Par ou Ímpar

valor = int(input())

def saida():
    for i in range(0 ,valor):
        A = int(input())
        if A == 0:
            print("NULL")
            continue
        if A % 2 == 0:
            if A > 0:
                print("EVEN POSITIVE")
            else:
                print("EVEN NEGATIVE")
        else:
            if A > 0:
                print("ODD POSITIVE")
            else:
                print("ODD NEGATIVE")

saida()