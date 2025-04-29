# 1041 - Coordenadas de um Ponto

valores = input().split()

x = float(valores[0])
y = float(valores[1])

# Q1 X > 0 e Y > 0
# Q2 X < 0 e Y > 0
# Q3 X < 0 e Y < 0
# Q4 x > 0 e Y < 0

if x == 0 and y == 0:
    print("Origem")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
elif y == 0:
    print("Eixo X")
elif x == 0:
    print("Eixo Y")