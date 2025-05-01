# 1097 - Sequencia IJ 3

def IJ():
    I = 1
    J = 7

    contador = 0

    for i in range (0, 15):
        print(f"I={I} J={J}")
        J = J - 1
        contador += 1
        if contador == 3:
            I = I + 2
            contador = 0
            J = J + 5

IJ()