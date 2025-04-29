# 1046 - Tempo de jogo

valores = input().split()

Inicio = int(valores[0])
Final = int(valores[1])

if Inicio > Final:
    A = 24 - Inicio
    duracao = A + Final
    print(f"O JOGO DUROU {duracao} HORA(S)")
elif Inicio == Final:
    print("O JOGO DUROU 24 HORA(S)")
else:
    duracao = Final - Inicio
    print(f"O JOGO DUROU {duracao} HORA(S)")