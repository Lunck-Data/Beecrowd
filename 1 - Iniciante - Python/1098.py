# 1098 - Sequencia IJ 4

def IJ():
    I = 0
    J = 0
    
    condicao = True
    contador = 0

    while condicao:
        J += 1
        contador += 1
        if I % 1 != 0 and J % 1 != 0:
            print(f"I={I:.1f} J={J:.1f}")
        elif I % 1 == 0.0 and J % 1 == 0:
            print(f"I={I:.0f} J={J:.0f}")
        elif I % 1 != 0 and J % 1 == 0:
            print(f"I={I:.1f} J={J:.0f}")
        elif I % 1 == 0 and not J % 1 != 0:
            print(f"I={I:.0f} J={J:.1f}")
        if contador == 3:
            I += 0.2
            J -= 2.8
            contador = 0
            I = round(I, 1)
            J = round(J, 1)
            if I > 2.0:
                condicao = False

IJ()