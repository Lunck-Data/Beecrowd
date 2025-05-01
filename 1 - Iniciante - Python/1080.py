# 1080 - Maior e Posição

lista = {}

for i in range (1, 101):
    A = int(input())
    lista[i] = A

lugar = 0
maior = 0

for chave, valor in lista.items():
    if valor > maior:
        maior = valor
        lugar = chave

print(maior)
print(lugar)