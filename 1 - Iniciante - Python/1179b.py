# 1179 - Preenchimento de Vetor IV

listaPar = []
listaImpar = []
contadorPar = 0
contadorImpar = 0

def PrintPar(contadorPar, listaPar):
    for i in range(0,contadorPar):
        print(f"par[{i}] = {listaPar[i]}")

def PrintImpar(contadorImpar, listaImpar):
    for i in range(0,contadorImpar):
        print(f"impar[{i}] = {listaImpar[i]}")

for i in range(0,15):
    X = int(input())

    if X % 2 == 0:
        listaPar.append(X)
        contadorPar += 1
        if contadorPar > 4:
            PrintPar(contadorPar, listaPar)
            contadorPar = 0
            listaPar.clear()
    else:
        listaImpar.append(X)
        contadorImpar += 1
        if contadorImpar > 4:
            PrintImpar(contadorImpar, listaImpar)
            contadorImpar = 0
            listaImpar.clear()

PrintImpar(contadorImpar, listaImpar)
PrintPar(contadorPar, listaPar)