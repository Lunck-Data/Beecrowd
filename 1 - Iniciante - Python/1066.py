# 1066 - Pares, Ímpares, Positivos e Negativos

lista = []

for A in range(0,5):
    A = int(input())
    lista.append(A)

contadorPares = 0
contadorImpar = 0
contadorPosi  = 0
contadorNega  = 0

for i in lista:
    if i % 2 == 0:
        contadorPares += 1
    else:
        contadorImpar += 1
    if i > 0:
        contadorPosi += 1
    elif i < 0:
        contadorNega += 1

print(f"{contadorPares} valor(es) par(es)")
print(f"{contadorImpar} valor(es) impar(es)")
print(f"{contadorPosi} valor(es) positivo(s)")
print(f"{contadorNega} valor(es) negativo(s)")