# 1158 - Soma de Ímpares Consecutivos III

valor = int(input())

for i in range (0,valor):
    valores = input().split()
    X = int(valores[0])
    Y = int(valores[1])
    
    if X % 2 == 0:
        X += 1
        
    soma = 0
    for e in range(0, Y):
        soma = soma + (X + (e * 2))
    
    print(soma)