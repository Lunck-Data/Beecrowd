
segundoInicio = int(input())
segundoFinal = int(input())

def segundos():
    if segundoInicio > segundoFinal:
        A = 60 - segundoInicio
        duracao = A + segundoFinal
        return duracao
    elif segundoInicio == segundoFinal:
        return 0
    else:
        duracao = segundoFinal - segundoInicio
        return duracao
    
print(segundos())