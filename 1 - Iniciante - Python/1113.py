# 1113 - Crescente e Decrescente

def desafio():
    
    condicao = True

    while condicao:
        valor = input().split()
        A = int(valor[0])
        B = int(valor[1])
        if A == B:
            break
        elif A > B:
            print("Decrescente")
        else:
            print("Crescente")
        
desafio()