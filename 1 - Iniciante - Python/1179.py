# 1179 - Preenchimento de Vetor IV

listaPar = []
listaImpar = []
listaRestoPar = []
listaRestoImpar = []

contadorPar = 0
contadorImpar = 0
loopPar = 0
loopImpar = 0
loopRestoPar = 0
loopRestoImpar = 0

for i in range(0,15):
    X = int(input())
    if X % 2 == 0:
        if contadorPar < 5:
            listaPar.append(X)
            contadorPar += 1
            loopPar += 1
        else:
            listaRestoPar.append(X)
            loopRestoPar += 1
    else:
        if contadorImpar < 5:
            listaImpar.append(X)
            contadorImpar += 1
            loopImpar += 1
        else:
            listaRestoImpar.append(X)
            loopRestoImpar += 1

for i in range(0,loopPar):
    print(f"par[{i}] = {listaPar[i]}")

for i in range(0,loopImpar):
    print(f"impar[{i}] = {listaImpar[i]}")

for i in range(0,loopRestoImpar):
    print(f"impar[{i}] = {listaRestoImpar[i]}")

for i in range(0,loopRestoPar):
    print(f"par[{i}] = {listaRestoPar[i]}")