# 1044 - Múltiplos

valores = input().split()

A = int(valores[0])
B = int(valores[1])

multiplos = list(range(100))

def mult():

    multiBool = True

    for numero in multiplos:
        validacao = A * numero
        if validacao == B:
            print("Sao Multiplos")
            multiBool = False

        validacao = B * numero
        if validacao == A:
            print("Sao Multiplos")
            multiBool = False

    if multiBool:
        print("Nao sao Multiplos")

mult()