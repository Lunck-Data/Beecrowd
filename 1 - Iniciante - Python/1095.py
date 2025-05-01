# 1095 - Sequência IJ 1

def IJ():
    I = 1
    J = 60

    for i in range(0,100):
        print(f"I={I} J={J}")
        I = I + 3
        J = J - 5
        if J < 0:    
            break

IJ()