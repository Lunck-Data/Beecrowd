# 1037 - Intervalo

valor = float(input())

if valor >= 0 and valor <= 25:
    print("Intervalo [0,25]")

elif valor >= 25.01 and valor <= 50:
    print("Intervalo (25,50]")

elif valor >= 50.01 and valor <= 75:
    print("Intervalo (50,75]")

elif valor >= 75.01 and valor <= 100:
    print("Intervalo (75,100]")

else:
    print("Fora de intervalo")