# 1160 - Crescimento Populacional

def populacional():

    T = int(input())

    for i in range (0, T):
        valores = input().split()

        PA = int(valores[0])
        PB = int(valores[1])
        G1 = float(valores[2])
        G2 = float(valores[3])

        for a in range(1, 102):
            if a == 101:
                print("Mais de 1 seculo.")
                break
            PA = PA + int((PA*(G1/100)))
            PB = PB + int((PB*(G2/100)))
            
            if PA > PB:
                print(f"{a} anos.")
                break

populacional()