# 1145 - Sequência Lógica 2


def sequencia():
    valores = input().split()

    A = int(valores[0])
    B = int(valores[1])

    lista = list(range(1,(B+1)))

    durante = B//A
    teste = B/A

    if not durante == teste:
        durante += 1

    for i in range(0, (durante)):

        listaPrint = []

        for i in range(0, A):
            if not lista:
                listaPrint = " ".join(listaPrint)
                return print(listaPrint)
            listaPrint.append(f"{lista[0]}")
            lista.remove(lista[0])

        listaPrint = " ".join(listaPrint)
        print(listaPrint)

sequencia()