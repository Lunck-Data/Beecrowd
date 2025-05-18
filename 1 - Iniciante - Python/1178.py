# 1178 - Preenchimento de Vetor III

X = float(input())

restante = X
lista = []

lista.append(restante)

for i in range(1,100):
    restante = restante / 2
    lista.append(restante)

for a in range(0,100):
    print(f"N[{a}] = {lista[a]:.3f}")