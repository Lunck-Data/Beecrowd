# 1118 - Várias Notas Com Validação

def validacao():

    condicao = True

    total = 0
    contador = 0

    while condicao:
        notas = float(input())
        if notas < 0 or notas > 10:
            print("nota invalida")
            continue
        total = total + notas
        contador += 1
        if contador == 2:
            media = total / 2
            print(f"media = {media:.2f}")
            break

validacao()

opcao = 0

while opcao == 0:
    print("novo calculo (1-sim 2-nao)")

    A = int(input())
    if A == 1:
        validacao()
    elif A == 2:
        opcao = 1
    else:
        continue