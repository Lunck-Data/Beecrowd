# 1047 - Tempo de Jogo com Minutos

valores = input().split()

horaInicial = int(valores[0]) # 10
minutoInicial = int(valores[1])
horaFinal = int(valores[2]) # 10
minutoFinal = int(valores[3])

def hora():
    if horaInicial > horaFinal:
        A = 24 - horaInicial
        duracao = A + horaFinal
        return duracao
    elif horaInicial == horaFinal:
        return 24
    else:
        duracao = horaFinal - horaInicial
        return duracao

def minuto():
    if minutoInicial > minutoFinal:
        A = 60 - minutoInicial
        duracao = A + minutoFinal
        return duracao
    elif minutoInicial == minutoFinal:
        return 0
    else:
        duracao = minutoFinal - minutoInicial
        return duracao
    
duracaoHora = hora()
duracaoMinuto = minuto()

if minutoInicial > minutoFinal:
    duracaoHora = duracaoHora - 1
    print(f"O JOGO DUROU {duracaoHora} HORA(S) E {duracaoMinuto} MINUTO(S)")
elif horaInicial == horaFinal and minutoInicial < minutoFinal:
    print(f"O JOGO DUROU 0 HORA(S) E {duracaoMinuto} MINUTO(S)")
elif minutoInicial < minutoFinal:
    print(f"O JOGO DUROU {duracaoHora} HORA(S) E {duracaoMinuto} MINUTO(S)")
else:
    print(f"O JOGO DUROU {duracaoHora} HORA(S) E {duracaoMinuto} MINUTO(S)")