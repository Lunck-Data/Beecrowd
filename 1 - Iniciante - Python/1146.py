# 1146 - Sequências Crescentes

def sequencias():

    while True:
        valor = int(input())

        if valor == 0:
            return

        lista = []

        for i in range (1, (valor+1)):
            lista.append(f"{i}")

        lista = " ".join(lista)
        print(lista)


sequencias()