# 1061 - Tempo de Evento

dia1 = input().split()
hora1 = input().split(' : ')
dia2 = input().split()
hora2 = input().split(' : ')

#Inicio
diaInicio = int(dia1[1])
horaInicio = int(hora1[0])
minutoInicio = int(hora1[1])
segundoInicio = int(hora1[2])

#Fim
diaFinal = int(dia2[1])
horaFinal = int(hora2[0])
minutoFinal = int(hora2[1])
segundoFinal = int(hora2[2])

def horas():
    if horaInicio > horaFinal:
        A = 24 - horaInicio
        duracao = A + horaFinal
        return duracao
    else:
        duracao = horaFinal - horaInicio
        return duracao

def minutos():
    if minutoInicio > minutoFinal:
        A = 60 - minutoInicio
        duracao = A + minutoFinal
        return duracao
    else:
        duracao = minutoFinal - minutoInicio
        return duracao
    
def segundos():
    if segundoInicio > segundoFinal:
        A = 60 - segundoInicio
        duracao = A + segundoFinal
        return duracao
    else:
        duracao = segundoFinal - segundoInicio
        return duracao

Dias = diaFinal - diaInicio
if horaInicio > horaFinal:
    Dias -= 1

print(f"{Dias} dia(s)")
print(f"{horas()} hora(s)")
print(f"{minutos()} minuto(s)")
print(f"{segundos()} segundo(s)")