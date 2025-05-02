# 1131 - Grenais

# 1 Inter 2 Grêmio

def grenais():

    totalGrenais = 0
    vInter = 0
    vGremio = 0
    empates = 0
    con = 0

    condicao = True

    while condicao:
        valor = input().split()
        I = int(valor[0])
        G = int(valor[1])
        
        totalGrenais += 1
        if I > G:
            vInter = vInter + 1
        elif G > I:
            vGremio = vGremio + 1
        elif G == I:
            empates = empates + 1
        
        print("Novo grenal (1-sim 2-nao)")
        con = int(input())
        if con == 1:
            continue
        elif con == 2:
            condicao = False

    print(f"{totalGrenais} grenais")
    print(f"Inter:{vInter}")
    print(f"Gremio:{vGremio}")
    print(f"Empates:{empates}")

    if vInter > vGremio:
        print("Inter venceu mais")
    elif vGremio > vInter:
        print("Gremio venceu mais")
    elif vGremio == vInter:
        print("Nao houve vencedor")

grenais()