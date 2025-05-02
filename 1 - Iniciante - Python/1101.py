# 1101 - Sequência de Números e Soma

def sequencia():
    condicao = True

    while condicao:
        valor = input().split()
        A = int(valor[0])
        B = int(valor[1])
        if A <= 0 or B <= 0:
            condicao = False
            continue
        if A > B:
            lista = list(range(B, (A+1)))
            soma = 0
            listona = []
            for i in lista:
                soma = soma + i
                listona.append(f"{i}")
            listona = " ".join(listona)
            print(f"{listona} Sum={soma}")
        else:
            lista = list(range(A, (B+1)))
            soma = 0
            listona = []
            for i in lista:
                soma = soma + i
                listona.append(f"{i}")
            listona = " ".join(listona)
            print(f"{listona} Sum={soma}")

sequencia()